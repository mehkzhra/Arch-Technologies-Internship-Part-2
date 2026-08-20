# Data Science — Month 2, Task 4

## Movie Rating Prediction

### Objective

The objective is to predict how a user may rate an unseen movie and generate useful movie recommendations from historical rating patterns.

### Dataset

The project uses MovieLens Latest Small from GroupLens. It contains 100,836 ratings across 9,742 movies created by 610 users. Ratings use a 0.5-to-5-star scale. The official dataset is automatically downloaded by the program on its first run.

### Tools and technologies

- Python
- Visual Studio Code
- pandas and NumPy
- scikit-learn
- Matplotlib and Seaborn
- joblib

### Methodology

The ratings are divided into 80% training and 20% testing data. User and movie statistics are calculated from training data only to reduce information leakage. These include each user's mean rating and rating count, each movie's mean rating and rating count, and simple movie metadata such as release year and genre count.

A Random Forest Regressor learns relationships between the user, movie, historical statistics, and final rating. Predictions are limited to MovieLens' valid 0.5–5.0 range. Model performance is evaluated using MAE, RMSE, and R² on unseen test ratings.

The program also predicts ratings for movies not previously rated by a sample active user and ranks the ten highest-scoring items as recommendations. An actual-versus-predicted plot and residual distribution visualize prediction performance.

### Evaluation metrics

- MAE measures the average absolute difference between actual and predicted ratings.
- RMSE gives greater weight to larger rating errors.
- R² measures how much variation in ratings is explained by the regression model.

### Result

The Movie Rating Prediction project implements a complete recommendation workflow: official dataset download, preprocessing, feature engineering, regression training, performance evaluation, visualization, unseen-movie scoring, recommendation ranking, and model export.

### Screenshot checklist

- MovieLens dataset statistics
- MAE, RMSE, and R²
- Actual-vs-predicted rating plot
- Prediction-error distribution
- Top movie recommendations
- Generated-file confirmation
