"""Iris Flower Classification - Arch Technologies Month 2, Task 4."""

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split


RANDOM_STATE = 42


def main() -> None:
    iris = load_iris(as_frame=True)
    features = iris.data.copy()
    target = iris.target.copy()

    print("Dataset shape:", features.shape)
    print("Missing values:", int(features.isnull().sum().sum()))
    print("Features:", list(features.columns))
    print("Species:", list(iris.target_names))

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=target,
    )

    model = RandomForestClassifier(
        n_estimators=150,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(
        y_test,
        predictions,
        target_names=iris.target_names,
        zero_division=0,
    )

    print(f"\nAccuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\nClassification Report:\n")
    print(report)

    matrix = confusion_matrix(y_test, predictions)
    importance = pd.Series(
        model.feature_importances_, index=features.columns
    ).sort_values(ascending=False)

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=iris.target_names,
        yticklabels=iris.target_names,
        ax=axes[0],
    )
    axes[0].set_title("Iris Confusion Matrix")
    axes[0].set_xlabel("Predicted Species")
    axes[0].set_ylabel("Actual Species")

    importance.sort_values().plot(
        kind="barh", ax=axes[1], color="#8b5cf6"
    )
    axes[1].set_title("Feature Importance")
    axes[1].set_xlabel("Importance Score")

    plt.tight_layout()
    plt.savefig("iris_model_results.png", dpi=180, bbox_inches="tight")
    plt.show()

    sample_flower = pd.DataFrame(
        [[5.1, 3.5, 1.4, 0.2]], columns=features.columns
    )
    sample_class = model.predict(sample_flower)[0]
    sample_probabilities = model.predict_proba(sample_flower)[0]

    print("\nSample flower measurements:")
    print(sample_flower.to_string(index=False))
    print("Predicted species:", iris.target_names[sample_class])
    print("Confidence:", f"{sample_probabilities[sample_class] * 100:.2f}%")

    model_package = {
        "model": model,
        "feature_names": list(features.columns),
        "target_names": list(iris.target_names),
    }
    joblib.dump(model_package, "iris_classifier.pkl")
    print("\nSaved: iris_classifier.pkl")
    print("Saved: iris_model_results.png")


if __name__ == "__main__":
    main()
