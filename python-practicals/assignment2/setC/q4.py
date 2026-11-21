import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine = pd.read_csv(url, sep=";")
print("Description:\n", wine.describe())
print("Mean of numeric attributes:\n", wine.mean())
print("Missing values:", wine.isnull().sum().sum())
