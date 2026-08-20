# Movie Rating Prediction

Arch Technologies Internship — Data Science, Month 2, Task 4.

## Project overview

This VS Code project predicts how a user may rate a movie they have not seen and produces a ranked list of recommended movies. It uses the MovieLens Latest Small dataset and a Random Forest regression model enriched with user-rating and movie-rating statistics.

## Dataset

- Source: GroupLens MovieLens
- Dataset: MovieLens Latest Small
- Ratings: 100,836
- Movies: 9,742
- Users: 610
- Rating scale: 0.5 to 5 stars

The script automatically downloads the official dataset on its first run and stores it in the local `data` folder. Later runs reuse that local copy.

Dataset page: https://grouplens.org/datasets/movielens/latest/

## Model workflow

- 80% training and 20% testing split
- User mean and rating-count features computed from training data
- Movie mean and rating-count features computed from training data
- Movie year and genre-count metadata
- Random Forest Regressor
- Predictions clipped to the valid 0.5–5.0 rating range
- Evaluation with MAE, RMSE, and R²
- Top-10 recommendations for a sample active user

## Requirements

- Python 3.10 or newer
- Visual Studio Code
- VS Code Python extension
- Internet connection on the first run

## Run in VS Code on Windows

Open this folder in VS Code and select **Terminal → New Terminal**.

Create a virtual environment:

```cmd
python -m venv venv
```

Activate it in CMD:

```cmd
venv\Scripts\activate
```

Install dependencies:

```cmd
pip install -r requirements.txt
```

Run the project:

```cmd
python movie_rating_prediction.py
```

Training can take a short while because the model uses more than 100,000 ratings.

## Expected output

The terminal displays:

- Ratings and movies dataset sizes
- Number of users and rated movies
- Missing-value check
- MAE, RMSE, and R²
- Top recommended movies for a sample user
- Generated-file confirmation

Generated files:

```text
movie_rating_model.pkl
movie_rating_results.png
top_recommendations.csv
```

## Screenshot requirements

Capture screenshots showing:

- VS Code with `movie_rating_prediction.py` open
- Dataset statistics in the terminal
- MAE, RMSE, and R²
- Actual-vs-predicted ratings graph
- Prediction-error distribution
- Top recommendations in the terminal
- Generated-file confirmation

Recommended names:

```text
movie_rating_metrics.png
movie_rating_results.png
movie_recommendations.png
```

## Folder structure

```text
Movie Rating Prediction/
├── movie_rating_prediction.py
├── requirements.txt
├── README.md
├── report_content.md
├── data/                         # created automatically
├── movie_rating_model.pkl        # generated after running
├── movie_rating_results.png      # generated after running
├── top_recommendations.csv       # generated after running
└── screenshots/
    ├── movie_rating_metrics.png
    ├── movie_rating_results.png
    └── movie_recommendations.png
```

Do not upload the `venv` folder to GitHub.

## Concepts demonstrated

Recommendation systems, regression, user/movie aggregate features, train/test evaluation, MAE, RMSE, R², ranking, data visualization, and model persistence.
