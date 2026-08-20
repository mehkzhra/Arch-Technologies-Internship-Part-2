"""Train and evaluate a CNN on the FER-2013 facial-emotion dataset."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = PROJECT_DIR / "dataset"
OUTPUT_DIR = PROJECT_DIR / "output"
MODEL_PATH = OUTPUT_DIR / "best_fer2013_cnn.pth"


class EmotionCNN(nn.Module):
    """Small CNN suitable for 48x48 grayscale FER-2013 images."""

    def __init__(self, num_classes: int = 7) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 6 * 6, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.4),
            nn.Linear(256, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.classifier(self.features(x))


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def data_transforms() -> tuple[transforms.Compose, transforms.Compose]:
    train_tfms = transforms.Compose(
        [
            transforms.Grayscale(num_output_channels=1),
            transforms.Resize((48, 48)),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(10),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,)),
        ]
    )
    test_tfms = transforms.Compose(
        [
            transforms.Grayscale(num_output_channels=1),
            transforms.Resize((48, 48)),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,)),
        ]
    )
    return train_tfms, test_tfms


def load_data(data_dir: Path, batch_size: int) -> tuple[DataLoader, DataLoader, list[str]]:
    train_dir, test_dir = data_dir / "train", data_dir / "test"
    if not train_dir.is_dir() or not test_dir.is_dir():
        raise FileNotFoundError(
            "FER-2013 folders not found. Expected dataset/train and dataset/test. "
            "See README.md for the exact download/extract steps."
        )

    train_tfms, test_tfms = data_transforms()
    train_ds = datasets.ImageFolder(train_dir, transform=train_tfms)
    test_ds = datasets.ImageFolder(test_dir, transform=test_tfms)
    if train_ds.classes != test_ds.classes:
        raise ValueError("Train and test emotion folders do not match.")

    pin_memory = torch.cuda.is_available()
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=0, pin_memory=pin_memory)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, num_workers=0, pin_memory=pin_memory)
    return train_loader, test_loader, train_ds.classes


def run_epoch(model, loader, loss_fn, device, optimizer=None) -> tuple[float, float]:
    training = optimizer is not None
    model.train(training)
    total_loss = correct = total = 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        if training:
            optimizer.zero_grad(set_to_none=True)
        with torch.set_grad_enabled(training):
            logits = model(images)
            loss = loss_fn(logits, labels)
            if training:
                loss.backward()
                optimizer.step()
        total_loss += loss.item() * labels.size(0)
        correct += (logits.argmax(1) == labels).sum().item()
        total += labels.size(0)

    return total_loss / total, correct / total


@torch.no_grad()
def collect_predictions(model, loader, device) -> tuple[list[int], list[int]]:
    model.eval()
    y_true, y_pred = [], []
    for images, labels in loader:
        logits = model(images.to(device))
        y_true.extend(labels.tolist())
        y_pred.extend(logits.argmax(1).cpu().tolist())
    return y_true, y_pred


def save_training_plot(history: dict[str, list[float]]) -> None:
    epochs = range(1, len(history["train_loss"]) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].plot(epochs, history["train_loss"], label="Train")
    axes[0].plot(epochs, history["test_loss"], label="Test")
    axes[0].set(title="CNN Loss", xlabel="Epoch", ylabel="Loss")
    axes[0].legend()
    axes[1].plot(epochs, history["train_acc"], label="Train")
    axes[1].plot(epochs, history["test_acc"], label="Test")
    axes[1].set(title="CNN Accuracy", xlabel="Epoch", ylabel="Accuracy")
    axes[1].legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "training_history.png", dpi=160)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="FER-2013 facial emotion recognition with a CNN")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_DIR, help="Dataset folder containing train/ and test/")
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--lr", type=float, default=1e-3)
    args = parser.parse_args()

    set_seed()
    OUTPUT_DIR.mkdir(exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_loader, test_loader, classes = load_data(args.data, args.batch_size)
    print(f"Training images: {len(train_loader.dataset):,}")
    print(f"Testing images : {len(test_loader.dataset):,}")
    print(f"Classes: {classes}")

    model = EmotionCNN(len(classes)).to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    history = {"train_loss": [], "test_loss": [], "train_acc": [], "test_acc": []}
    best_acc = -1.0

    for epoch in range(1, args.epochs + 1):
        train_loss, train_acc = run_epoch(model, train_loader, loss_fn, device, optimizer)
        test_loss, test_acc = run_epoch(model, test_loader, loss_fn, device)
        for key, value in (("train_loss", train_loss), ("test_loss", test_loss), ("train_acc", train_acc), ("test_acc", test_acc)):
            history[key].append(value)
        print(f"Epoch {epoch:02d}/{args.epochs} | train acc {train_acc:.4f} | test acc {test_acc:.4f}")

        if test_acc > best_acc:
            best_acc = test_acc
            torch.save({"model_state": model.state_dict(), "classes": classes, "test_accuracy": test_acc}, MODEL_PATH)

    checkpoint = torch.load(MODEL_PATH, map_location=device, weights_only=True)
    model.load_state_dict(checkpoint["model_state"])
    y_true, y_pred = collect_predictions(model, test_loader, device)
    report = classification_report(y_true, y_pred, target_names=classes, digits=4, zero_division=0)
    (OUTPUT_DIR / "classification_report.txt").write_text(report, encoding="utf-8")
    (OUTPUT_DIR / "metrics.json").write_text(json.dumps({"best_test_accuracy": best_acc}, indent=2), encoding="utf-8")
    save_training_plot(history)

    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(cm, display_labels=classes)
    fig, ax = plt.subplots(figsize=(9, 8))
    disp.plot(ax=ax, xticks_rotation=45, colorbar=False)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=160)
    plt.close(fig)

    print("\nClassification Report\n", report)
    print(f"Best test accuracy: {best_acc:.4f}")
    print(f"Saved model/results in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
