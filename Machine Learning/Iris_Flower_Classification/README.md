# Iris Flower Classification

Arch Technologies Internship — Machine Learning, Month 2, Task 4.

## Project overview

This VS Code project trains a machine-learning classifier to identify Iris flowers as Setosa, Versicolor, or Virginica using sepal length, sepal width, petal length, and petal width.

The canonical Iris dataset is loaded directly from scikit-learn. It contains the same standard observations commonly distributed through Kaggle, without requiring credentials or a manual CSV download.

## Model details

- Algorithm: Random Forest Classifier
- Split: 80% training and 20% testing
- Stratified splitting preserves all three classes
- Metrics: accuracy, precision, recall, and F1-score
- Visualizations: confusion matrix and feature importance
- Random state: 42

## Requirements

- Python 3.10 or newer
- Visual Studio Code
- VS Code Python extension

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

Install the packages:

```cmd
pip install -r requirements.txt
```

Run the project:

```cmd
python iris_flower_classification.py
```

If VS Code requests an interpreter, press `Ctrl + Shift + P`, select **Python: Select Interpreter**, and choose the interpreter inside `venv`.

## Program output

The program displays:

- Dataset shape and missing-value check
- Model accuracy
- Classification report for all three species
- Confusion matrix
- Feature-importance chart
- Prediction and confidence for a sample flower

It also creates:

```text
iris_classifier.pkl
iris_model_results.png
```

## Screenshot requirements

Capture screenshots showing:

- VS Code with the Python source open
- Terminal with accuracy and classification report
- Confusion matrix
- Feature-importance chart
- Sample flower prediction
- Saved-file confirmation

Recommended names:

```text
iris_metrics.png
iris_model_results.png
```

## Folder structure

```text
Iris Flower Classification/
├── iris_flower_classification.py
├── requirements.txt
├── README.md
├── report_content.md
├── iris_classifier.pkl          # generated after running
├── iris_model_results.png       # generated after running
└── screenshots/
    ├── iris_metrics.png
    └── iris_model_results.png
```

Do not upload the `venv` folder to GitHub.

## Concepts demonstrated

Multi-class classification, train/test splitting, stratification, Random Forests, accuracy, precision, recall, F1-score, confusion matrices, feature importance, probability prediction, and model persistence.
