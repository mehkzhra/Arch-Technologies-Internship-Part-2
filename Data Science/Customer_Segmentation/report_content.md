# Data Science — Month 2, Task 3

## Customer Segmentation using K-Means

### Objective

The objective is to group customers into meaningful segments based on purchasing behavior and identify the characteristics of each segment using K-Means clustering.

### Dataset

The project uses the public Mall Customer Segmentation Data dataset from Kaggle. It contains customer attributes including gender, age, annual income, and spending score. Annual Income and Spending Score are selected as the main clustering dimensions because they directly support customer-value and purchasing-behavior analysis.

### Tools and technologies

- Python
- Visual Studio Code
- KaggleHub
- pandas
- scikit-learn
- Matplotlib and Seaborn
- joblib

### Methodology

The dataset is downloaded from Kaggle, loaded into pandas, and inspected for dimensions, columns, and missing values. Annual Income and Spending Score are standardized with `StandardScaler` so both features contribute on a comparable scale.

The elbow method is evaluated over cluster counts from 2 to 10. Five clusters are then fitted with K-Means using a fixed random state. The silhouette score provides a quantitative measure of cluster separation. Each cluster is profiled through mean, minimum, maximum, and customer-count statistics.

A scatter plot visualizes the final customer groups and their centroids. The labeled dataset is exported to CSV, while the fitted K-Means model and scaler are saved with joblib.

### Segment interpretation

The five clusters typically reveal groups such as high-income/high-spending customers, high-income/low-spending customers, lower-income/high-spending customers, lower-income/low-spending customers, and customers with moderate income and spending. Exact cluster numbers are arbitrary, so the behavioral statistics are used to interpret each segment.

### Result

The Customer Segmentation project was completed successfully. K-Means clustering separates customers into interpretable groups, the elbow curve and silhouette score support evaluation, and the final visualization clearly shows the discovered customer segments.

### Screenshot checklist

- Dataset information and missing-value check
- Silhouette score and cluster summary
- Elbow Method plot
- Customer Segments scatter plot with centroids
- Generated-file confirmation
