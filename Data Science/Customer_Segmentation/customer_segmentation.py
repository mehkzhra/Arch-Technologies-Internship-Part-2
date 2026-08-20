"""Customer Segmentation with K-Means - Arch Technologies Month 2, Task 3."""

from pathlib import Path

import joblib
import kagglehub
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


DATASET_HANDLE = "vjchoudhary7/customer-segmentation-tutorial-in-python"
RANDOM_STATE = 42


def find_customer_csv(folder: Path) -> Path:
    """Return the first CSV file found in the downloaded dataset folder."""
    csv_files = sorted(folder.rglob("*.csv"))
    if not csv_files:
        raise FileNotFoundError("No CSV file was found in the downloaded dataset.")
    return csv_files[0]


def load_dataset() -> pd.DataFrame:
    """Download the public Kaggle dataset and return it as a DataFrame."""
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    existing_files = sorted(data_folder.rglob("*.csv"))
    if existing_files:
        csv_path = existing_files[0]
        print(f"Using existing dataset: {csv_path}")
    else:
        print("Downloading customer dataset from Kaggle...")
        downloaded_path = Path(
            kagglehub.dataset_download(DATASET_HANDLE, output_dir=str(data_folder))
        )
        csv_path = find_customer_csv(downloaded_path if downloaded_path.is_dir() else data_folder)
        print(f"Dataset downloaded: {csv_path}")

    return pd.read_csv(csv_path)


def get_feature_columns(df: pd.DataFrame) -> tuple[str, str]:
    """Locate the income and spending-score columns across common name variants."""
    normalized = {column.lower().replace(" ", ""): column for column in df.columns}

    income_column = next(
        (
            original
            for normalized_name, original in normalized.items()
            if "annualincome" in normalized_name
        ),
        None,
    )
    spending_column = next(
        (
            original
            for normalized_name, original in normalized.items()
            if "spendingscore" in normalized_name
        ),
        None,
    )

    if income_column is None or spending_column is None:
        raise ValueError(
            "Expected Annual Income and Spending Score columns were not found. "
            f"Available columns: {list(df.columns)}"
        )

    return income_column, spending_column


def main() -> None:
    customers = load_dataset()
    print("\nDataset shape:", customers.shape)
    print("Columns:", list(customers.columns))
    print("Missing values:", int(customers.isnull().sum().sum()))

    income_column, spending_column = get_feature_columns(customers)
    features = customers[[income_column, spending_column]].dropna().copy()

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    inertia_values = []
    candidate_clusters = range(2, 11)
    for cluster_count in candidate_clusters:
        candidate_model = KMeans(
            n_clusters=cluster_count,
            random_state=RANDOM_STATE,
            n_init=10,
        )
        candidate_model.fit(scaled_features)
        inertia_values.append(candidate_model.inertia_)

    cluster_count = 5
    model = KMeans(
        n_clusters=cluster_count,
        random_state=RANDOM_STATE,
        n_init=10,
    )
    cluster_labels = model.fit_predict(scaled_features)

    features["Cluster"] = cluster_labels
    customers.loc[features.index, "Cluster"] = cluster_labels
    customers["Cluster"] = customers["Cluster"].astype("Int64")

    silhouette = silhouette_score(scaled_features, cluster_labels)
    print(f"\nSelected clusters: {cluster_count}")
    print(f"Silhouette score: {silhouette:.4f}")

    summary = (
        features.groupby("Cluster")[[income_column, spending_column]]
        .agg(["mean", "min", "max", "count"])
        .round(2)
    )
    print("\nCluster summary:\n")
    print(summary.to_string())

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    axes[0].plot(list(candidate_clusters), inertia_values, marker="o", color="#2563eb")
    axes[0].set_title("Elbow Method for K-Means")
    axes[0].set_xlabel("Number of Clusters")
    axes[0].set_ylabel("Inertia")
    axes[0].set_xticks(list(candidate_clusters))

    sns.scatterplot(
        data=features,
        x=income_column,
        y=spending_column,
        hue="Cluster",
        palette="tab10",
        s=75,
        alpha=0.8,
        ax=axes[1],
    )
    axes[1].set_title("Customer Segments")

    centers = scaler.inverse_transform(model.cluster_centers_)
    axes[1].scatter(
        centers[:, 0],
        centers[:, 1],
        c="black",
        marker="X",
        s=220,
        label="Centroids",
    )
    axes[1].legend(title="Cluster")

    plt.tight_layout()
    plt.savefig("customer_segments.png", dpi=180, bbox_inches="tight")
    plt.show()

    customers.to_csv("clustered_customers.csv", index=False)
    joblib.dump(
        {
            "model": model,
            "scaler": scaler,
            "features": [income_column, spending_column],
        },
        "kmeans_customer_segmentation.pkl",
    )

    print("\nSaved: clustered_customers.csv")
    print("Saved: customer_segments.png")
    print("Saved: kmeans_customer_segmentation.pkl")


if __name__ == "__main__":
    main()
