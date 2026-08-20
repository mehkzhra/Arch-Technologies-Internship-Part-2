# California Housing Price Prediction

Arch Technologies Internship — Machine Learning, Month 2, Task 3.

## Project overview

This VS Code project trains a regression model to predict median house values in California using location, population, income, household, and room-related features. It performs data inspection, train/test splitting, Random Forest training, evaluation, visualization, feature-importance analysis, and model export.

The canonical California Housing dataset is loaded automatically through scikit-learn, so no Kaggle credentials or manual dataset download is required.

## Model details

- Algorithm: Random Forest Regressor
- Training/testing split: 80%/20%
- Evaluation metrics: MAE, RMSE, and R²
- Visualizations: actual-versus-predicted values and feature importance
- Random state: 42 for reproducibility

The target is measured in units of USD 100,000. For example, `2.5` represents approximately USD 250,000.

## Requirements

- Python 3.10 or newer
- Visual Studio Code
- VS Code Python extension
- Internet connection for the dataset's first download

## Run in VS Code on Windows

### 1. Open the folder

Extract the ZIP. In VS Code, select **File → Open Folder** and choose the `Housing Price Prediction` folder.

### 2. Open the terminal

Select **Terminal → New Terminal**. Confirm that the terminal is inside the project folder.

### 3. Create a virtual environment

```cmd
python -m venv venv
```

### 4. Activate the environment

In CMD:

```cmd
venv\Scripts\activate
```

If VS Code uses PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```cmd
pip install -r requirements.txt
```

### 6. Run the program

```cmd
python housing_price_prediction.py
```

The first run downloads the canonical California Housing dataset. The program then trains the model, prints the evaluation metrics, displays the charts, and saves the trained model.

## Expected terminal output

The exact metric values can vary slightly by package version, but the output will follow this format:

```text
Dataset shape: (20640, 8)
Missing values: 0
Feature names: ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
MAE:  ...
RMSE: ...
R2:   ...
Note: target values are measured in units of $100,000.
Saved: california_housing_model.pkl
Saved: housing_model_results.png
```

## Generated files

- `california_housing_model.pkl` — trained Random Forest model
- `housing_model_results.png` — actual-versus-predicted and feature-importance charts

## Screenshot requirements

Capture clear screenshots showing:

- VS Code with `housing_price_prediction.py` open
- Terminal showing dataset shape and zero missing values
- MAE, RMSE, and R² results
- Actual-versus-predicted chart
- Feature-importance chart
- Confirmation that the model and chart were saved

Recommended screenshot names:

```text
housing_metrics.png
housing_model_results.png
```

## Folder structure

```text
Housing Price Prediction/
├── housing_price_prediction.py
├── requirements.txt
├── README.md
├── report_content.md
├── california_housing_model.pkl       # generated after running
├── housing_model_results.png          # generated after running
└── screenshots/
    ├── housing_metrics.png
    └── housing_model_results.png
```

Do not upload the `venv` folder to GitHub.

## Concepts demonstrated

Regression, dataset inspection, train/test splitting, ensemble learning, performance metrics, data visualization, feature importance, reproducibility, and model persistence.
