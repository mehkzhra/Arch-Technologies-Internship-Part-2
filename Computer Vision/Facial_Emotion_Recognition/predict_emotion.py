"""Predict the emotion in one cropped face image using the trained CNN."""

from __future__ import annotations

import argparse
from pathlib import Path

import torch
from PIL import Image

from facial_emotion_recognition import EmotionCNN, MODEL_PATH, data_transforms


def main() -> None:
    parser = argparse.ArgumentParser(description="Predict emotion from one face image")
    parser.add_argument("image", type=Path, help="Path to a face image")
    parser.add_argument("--model", type=Path, default=MODEL_PATH)
    args = parser.parse_args()

    if not args.image.is_file():
        raise FileNotFoundError(f"Image not found: {args.image}")
    if not args.model.is_file():
        raise FileNotFoundError("Trained model not found. Run facial_emotion_recognition.py first.")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint = torch.load(args.model, map_location=device, weights_only=True)
    classes = checkpoint["classes"]
    model = EmotionCNN(len(classes)).to(device)
    model.load_state_dict(checkpoint["model_state"])
    model.eval()

    _, inference_tfms = data_transforms()
    image = Image.open(args.image).convert("L")
    tensor = inference_tfms(image).unsqueeze(0).to(device)
    with torch.no_grad():
        probabilities = torch.softmax(model(tensor), dim=1)[0]
    confidence, index = probabilities.max(dim=0)

    print(f"Predicted emotion: {classes[index.item()]}")
    print(f"Confidence: {confidence.item() * 100:.2f}%")


if __name__ == "__main__":
    main()
