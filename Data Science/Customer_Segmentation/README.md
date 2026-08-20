# Customer Segmentation using K-Means

Arch Technologies Internship — Data Science, Month 2, Task 3.

## Project overview

This VS Code project groups customers into meaningful segments based on purchasing-related behavior using K-Means clustering. It uses the public **Mall Customer Segmentation Data** dataset from Kaggle and analyzes Annual Income and Spending Score.

The script automatically downloads the public dataset on the first run using KaggleHub. Later runs reuse the local copy stored inside the `data` folder.

## Dataset

- Source: Kaggle
- Dataset: Mall Customer Segmentation Data
- Kaggle handle: `vjchoudhary7/customer-segmentation-tutorial-in-python`
- Main clustering features: Annual Income and Spending Score

## Analysis performed

- Dataset loading and inspection
- Missing-value check
- Feature standardization with `StandardScaler`
- Elbow method for cluster analysis
- K-Means clustering with 5 customer groups
- Silhouette score evaluation
- Cluster statistics and interpretation
- Customer-segment visualization with centroids
- Export of clustered records and trained preprocessing/model objects

## Requirements

- Python 3.10 or newer
- Visual Studio Code
- VS Code Python extension
- Internet connection on the first run

The dataset is public. If Kaggle asks for authentication in your environment, sign in to Kaggle and configure Kaggle credentials before rerunning the script.

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
python customer_segmentation.py
```

## Expected output

The terminal will display:

- Dataset shape and columns
- Missing-value count
- Selected cluster count
- Silhouette score
- Mean/min/max/count statistics for each cluster
- Confirmation of generated files

The project creates:

```text
clustered_customers.csv
customer_segments.png
kmeans_customer_segmentation.pkl
```

## Screenshot requirements

Capture screenshots showing:

- VS Code with `customer_segmentation.py` open
- Dataset shape and silhouette score in the terminal
- Cluster summary in the terminal
- Elbow Method graph
- Customer Segments scatter plot
- Generated-file confirmation

Recommended names:

```text
customer_segmentation_metrics.png
customer_segments.png
```

## Folder structure

```text
Customer Segmentation/
├── customer_segmentation.py
├── requirements.txt
├── README.md
├── report_content.md
├── data/                              # created on first run
├── clustered_customers.csv            # generated after running
├── customer_segments.png              # generated after running
├── kmeans_customer_segmentation.pkl   # generated after running
└── screenshots/
    ├── customer_segmentation_metrics.png
    └── customer_segments.png
```

Do not upload the `venv` folder to GitHub.

## Concepts demonstrated

Unsupervised learning, K-Means clustering, feature scaling, the elbow method, silhouette score, cluster profiling, data visualization, and model persistence.
