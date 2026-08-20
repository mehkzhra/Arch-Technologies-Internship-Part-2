"""Movie Rating Prediction - Arch Technologies Month 2, Task 4."""

from pathlib import Path
from urllib.request import urlopen
import zipfile

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


DATASET_URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
RANDOM_STATE = 42
DATA_DIR = Path("data")


def download_movielens() -> tuple[Path, Path]:
    """Download and extract MovieLens Latest Small when it is not already present."""
    ratings_path = DATA_DIR / "ml-latest-small" / "ratings.csv"
    movies_path = DATA_DIR / "ml-latest-small" / "movies.csv"

    if ratings_path.exists() and movies_path.exists():
        print("Using existing MovieLens dataset.")
        return ratings_path, movies_path

    DATA_DIR.mkdir(exist_ok=True)
    zip_path = DATA_DIR / "ml-latest-small.zip"

    print("Downloading MovieLens Latest Small dataset...")
    with urlopen(DATASET_URL, timeout=120) as response:
        zip_path.write_bytes(response.read())

    with zipfile.ZipFile(zip_path, "r") as archive:
        archive.extractall(DATA_DIR)

    print("Dataset downloaded and extracted successfully.")
    return ratings_path, movies_path


def prepare_movies(movies: pd.DataFrame) -> pd.DataFrame:
    """Create lightweight numeric metadata from MovieLens movie information."""
    result = movies.copy()
    result["year"] = pd.to_numeric(
        result["title"].str.extract(r"\((\d{4})\)\s*$")[0], errors="coerce"
    )
    result["genre_count"] = result["genres"].fillna("").str.count(r"\|") + 1
    result.loc[result["genres"] == "(no genres listed)", "genre_count"] = 0
    return result


def build_rating_statistics(train: pd.DataFrame) -> tuple[float, pd.DataFrame, pd.DataFrame]:
    """Build user/movie rating summaries using training data only."""
    global_mean = float(train["rating"].mean())

    user_stats = (
        train.groupby("userId")["rating"]
        .agg(["mean", "count"])
        .rename(columns={"mean": "user_mean", "count": "user_count"})
        .reset_index()
    )
    movie_stats = (
        train.groupby("movieId")["rating"]
        .agg(["mean", "count"])
        .rename(columns={"mean": "movie_mean", "count": "movie_count"})
        .reset_index()
    )
    return global_mean, user_stats, movie_stats


def engineer_features(
    ratings: pd.DataFrame,
    movies: pd.DataFrame,
    global_mean: float,
    user_stats: pd.DataFrame,
    movie_stats: pd.DataFrame,
) -> pd.DataFrame:
    """Create regression features for user/movie rating pairs."""
    enriched = ratings.merge(user_stats, on="userId", how="left")
    enriched = enriched.merge(movie_stats, on="movieId", how="left")
    enriched = enriched.merge(
        movies[["movieId", "year", "genre_count"]], on="movieId", how="left"
    )

    enriched["user_mean"] = enriched["user_mean"].fillna(global_mean)
    enriched["movie_mean"] = enriched["movie_mean"].fillna(global_mean)
    enriched["user_count"] = enriched["user_count"].fillna(0)
    enriched["movie_count"] = enriched["movie_count"].fillna(0)
    enriched["year"] = enriched["year"].fillna(movies["year"].median())
    enriched["genre_count"] = enriched["genre_count"].fillna(0)
    return enriched


def feature_columns() -> list[str]:
    return [
        "userId",
        "movieId",
        "user_mean",
        "user_count",
        "movie_mean",
        "movie_count",
        "year",
        "genre_count",
    ]


def recommend_movies(
    user_id: int,
    ratings: pd.DataFrame,
    movies: pd.DataFrame,
    model: RandomForestRegressor,
    global_mean: float,
    user_stats: pd.DataFrame,
    movie_stats: pd.DataFrame,
    limit: int = 10,
) -> pd.DataFrame:
    """Predict ratings for unseen movies and return the highest-ranked items."""
    rated_movie_ids = set(ratings.loc[ratings["userId"] == user_id, "movieId"])
    candidates = movies.loc[~movies["movieId"].isin(rated_movie_ids), ["movieId"]].copy()
    candidates["userId"] = user_id

    candidate_features = engineer_features(
        candidates, movies, global_mean, user_stats, movie_stats
    )
    predicted = model.predict(candidate_features[feature_columns()])
    candidates["predicted_rating"] = np.clip(predicted, 0.5, 5.0)

    recommendations = candidates.merge(
        movies[["movieId", "title", "genres"]], on="movieId", how="left"
    )
    return recommendations.sort_values("predicted_rating", ascending=False).head(limit)


def main() -> None:
    ratings_path, movies_path = download_movielens()
    ratings = pd.read_csv(ratings_path)
    movies = prepare_movies(pd.read_csv(movies_path))

    print("\nRatings shape:", ratings.shape)
    print("Movies shape:", movies.shape)
    print("Users:", ratings["userId"].nunique())
    print("Rated movies:", ratings["movieId"].nunique())
    print("Missing rating values:", int(ratings["rating"].isnull().sum()))

    train, test = train_test_split(
        ratings,
        test_size=0.20,
        random_state=RANDOM_STATE,
    )
    global_mean, user_stats, movie_stats = build_rating_statistics(train)

    train_enriched = engineer_features(
        train, movies, global_mean, user_stats, movie_stats
    )
    test_enriched = engineer_features(
        test, movies, global_mean, user_stats, movie_stats
    )

    columns = feature_columns()
    model = RandomForestRegressor(
        n_estimators=150,
        max_depth=18,
        min_samples_leaf=3,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(train_enriched[columns], train_enriched["rating"])

    predictions = np.clip(model.predict(test_enriched[columns]), 0.5, 5.0)
    actual = test_enriched["rating"].to_numpy()

    mae = mean_absolute_error(actual, predictions)
    rmse = np.sqrt(mean_squared_error(actual, predictions))
    r2 = r2_score(actual, predictions)

    print(f"\nMAE:  {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2:   {r2:.4f}")

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].scatter(actual, predictions, alpha=0.2, color="#2563eb", s=18)
    axes[0].plot([0.5, 5], [0.5, 5], "r--")
    axes[0].set_title("Actual vs Predicted Ratings")
    axes[0].set_xlabel("Actual Rating")
    axes[0].set_ylabel("Predicted Rating")

    residuals = actual - predictions
    sns.histplot(residuals, bins=30, kde=True, color="#14b8a6", ax=axes[1])
    axes[1].axvline(0, color="black", linestyle="--")
    axes[1].set_title("Prediction Error Distribution")
    axes[1].set_xlabel("Actual - Predicted Rating")

    plt.tight_layout()
    plt.savefig("movie_rating_results.png", dpi=180, bbox_inches="tight")
    plt.show()

    sample_user = int(ratings["userId"].value_counts().index[0])
    recommendations = recommend_movies(
        sample_user,
        ratings,
        movies,
        model,
        global_mean,
        user_stats,
        movie_stats,
    )

    print(f"\nTop recommendations for user {sample_user}:\n")
    print(
        recommendations[["title", "predicted_rating"]]
        .to_string(index=False, formatters={"predicted_rating": "{:.2f}".format})
    )
    recommendations.to_csv("top_recommendations.csv", index=False)

    joblib.dump(
        {
            "model": model,
            "global_mean": global_mean,
            "user_stats": user_stats,
            "movie_stats": movie_stats,
            "feature_columns": columns,
        },
        "movie_rating_model.pkl",
        compress=3,
    )

    print("\nSaved: movie_rating_model.pkl")
    print("Saved: movie_rating_results.png")
    print("Saved: top_recommendations.csv")


if __name__ == "__main__":
    main()
