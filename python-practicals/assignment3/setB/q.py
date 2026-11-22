import pandas as pd
from sklearn.preprocessing import (
    Binarizer,
    MinMaxScaler,
    Normalizer,
    StandardScaler,
)

# Q1. Import the local winequality-red.csv (saved from the UCI link)
wine = pd.read_csv("../../winequality-red.csv", sep=";")

# Q2. Rescaling using MinMaxScaler
print(
    "MinMax scaled (0 to 1):\n",
    pd.DataFrame(MinMaxScaler().fit_transform(wine), columns=wine.columns).head(),
)

# Q3. Standardizing - mean 0 and standard deviation 1
print(
    "Standardized (mean 0, std 1):\n",
    pd.DataFrame(StandardScaler().fit_transform(wine), columns=wine.columns).head(),
)

# Q4. Normalizing - rescale each observation to unit norm using Normalizer
print(
    "Normalized to unit norm:\n",
    pd.DataFrame(Normalizer().transform(wine), columns=wine.columns).head(),
)

# Q5. Binarizing using Binarizer (threshold)
print(
    "Binarized (threshold 5):\n",
    pd.DataFrame(Binarizer(threshold=5).transform(wine), columns=wine.columns).head(),
)
