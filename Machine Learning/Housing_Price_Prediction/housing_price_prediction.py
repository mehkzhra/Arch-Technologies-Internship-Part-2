"""California Housing Price Prediction - Arch Technologies Month 2, Task 3."""

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


RANDOM_STATE = 42


def load_data() -> tuple[pd.DataFrame, pd.Series]:
    """Load the canonical California Housing dataset as pandas objects."""
    housing = fetch_california_housing(as_frame=True)
    features = housing.data.copy()
    target = housing.target.copy()
    return features, target


def main() -> None:
    features, target = load_data()

    print("Dataset shape:", features.shape)
    print("Missing values:", int(features.isnull().sum().sum()))
    print("Feature names:", list(features.columns))

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.20,
        random_state=RANDOM_STATE,
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=18,
        min_samples_leaf=2,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print(f"MAE:  {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2:   {r2:.4f}")
    print("Note: target values are measured in units of $100,000.")

    importance = pd.Series(
        model.feature_importances_, index=features.columns
    ).sort_values(ascending=False)

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].scatter(y_test, predictions, alpha=0.35, color="#2563eb")
    minimum = min(y_test.min(), predictions.min())
    maximum = max(y_test.max(), predictions.max())
    axes[0].plot([minimum, maximum], [minimum, maximum], "r--")
    axes[0].set_title("Actual vs Predicted House Values")
    axes[0].set_xlabel("Actual value ($100,000s)")
    axes[0].set_ylabel("Predicted value ($100,000s)")

    importance.sort_values().plot(
        kind="barh", ax=axes[1], color="#14b8a6"
    )
    axes[1].set_title("Feature Importance")
    axes[1].set_xlabel("Importance score")

    plt.tight_layout()
    plt.savefig("housing_model_results.png", dpi=180, bbox_inches="tight")
    plt.show()

    joblib.dump(model, "california_housing_model.pkl")
    print("Saved: california_housing_model.pkl")
    print("Saved: housing_model_results.png")


if __name__ == "__main__":
    main()
