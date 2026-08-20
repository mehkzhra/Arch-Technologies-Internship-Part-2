# Machine Learning — Month 2, Task 4

## Iris Flower Classification

### Objective

The objective is to build a machine-learning model that classifies Iris flowers into Setosa, Versicolor, or Virginica based on sepal and petal measurements.

### Dataset

The Iris dataset contains 150 observations, four numerical input features, and three balanced target classes. Each class represents one Iris species. The canonical dataset is loaded from scikit-learn, which provides the standard Iris data without requiring a separate download.

### Tools and technologies

- Python
- Visual Studio Code
- pandas
- scikit-learn
- Matplotlib and Seaborn
- joblib

### Methodology

The dataset is inspected for its dimensions, features, species names, and missing values. It is divided into 80% training and 20% testing data using stratified sampling. A Random Forest Classifier containing 150 decision trees is trained on the four measurements.

The trained model is evaluated on unseen test records using accuracy, precision, recall, F1-score, a classification report, and a confusion matrix. Feature-importance scores show which measurements contribute most strongly to classification. A new sample flower is classified with an associated probability, and the model is exported using joblib.

### Evaluation metrics

- Accuracy measures the proportion of correct classifications.
- Precision measures how many predicted instances of a species are correct.
- Recall measures how many actual instances of a species are identified.
- F1-score balances precision and recall.
- The confusion matrix displays correct and incorrect predictions for every class.

### Result

The Iris Flower Classification project was completed successfully. The Random Forest model distinguishes all three species with high accuracy, provides interpretable evaluation results, predicts a new flower, and saves the trained classifier for future use.

### Screenshot checklist

- Dataset information and missing-value result
- Accuracy and classification report
- Confusion matrix
- Feature-importance chart
- New flower prediction and confidence
- Saved model confirmation
