# Machine Learning — Month 2, Task 3

## California Housing Price Prediction

### Objective

The objective is to build and evaluate a machine-learning model that predicts California median house values from demographic, geographical, and housing-related features.

### Dataset

The California Housing dataset contains 20,640 observations and eight input features: median income, house age, average rooms, average bedrooms, population, average occupancy, latitude, and longitude. The target represents median house value in units of USD 100,000. The canonical dataset is loaded using scikit-learn, avoiding separate credentials while retaining the standard data required by the assignment.

### Tools and technologies

- Python
- Visual Studio Code
- pandas and NumPy
- scikit-learn
- Matplotlib and Seaborn
- joblib

### Methodology

The dataset is inspected for its shape, feature names, descriptive statistics, and missing values. The input features and target are divided into 80% training and 20% testing subsets with a fixed random state. A Random Forest Regressor is trained using 200 decision trees. Predictions on the unseen test set are evaluated using MAE, RMSE, and R².

An actual-versus-predicted scatter plot is used to assess prediction alignment. Random Forest feature-importance scores identify the variables that contribute most strongly to the predictions. Finally, the trained model is saved with joblib.

### Evaluation metrics

- MAE measures the average absolute prediction error.
- RMSE gives greater weight to large prediction errors.
- R² measures the proportion of variance explained by the model; values closer to 1 indicate better performance.

Exact results can vary slightly by library version, but the fixed random state ensures reproducible data splitting and model behavior.

### Result

The California Housing Price Prediction system was completed successfully. The Random Forest model learns non-linear relationships in the dataset, produces predictions for unseen records, reports appropriate regression metrics, visualizes prediction quality, and exports the trained model for reuse.

### Screenshot checklist

- Dataset shape and missing-value check
- Model evaluation metrics
- Actual-versus-predicted plot
- Feature-importance plot
- Model saving confirmation
