import numpy as np
import pandas as pd

# Q1. Minkowski distance between two points
p = np.array([1, 2, 3])
q = np.array([4, 6, 8])
r = 3
print("Minkowski distance:", np.sum(np.abs(p - q) ** r) ** (1 / r))

# Q2. Weighted average along specified axis of a flattened array
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
w = np.array([1, 2, 2])
print("Original flattened array:\n", a)
print("Weighted average along axis 1:\n", np.average(a, axis=1, weights=w))

# Q3. Cross-correlation of two arrays
a1 = np.array([0, 1, 3])
a2 = np.array([2, 4, 5])
print("Original array1:", a1)
print("Original array2:", a2)
print("Cross-correlation of the said arrays:\n", np.cov(a1, a2))

# Q4. Any UCI dataset (not iris), describe, mean of numeric attribute, check missing
wine = pd.read_csv("../../winequality-red.csv", sep=";")
print("Description:\n", wine.describe())
print("Mean of numeric attributes:\n", wine.mean(numeric_only=True))
print("Missing values:", wine.isnull().sum().sum())

# Q5. Nursery dataset - split on one categorical attribute using groupby, compare means
cols = [
    "parents",
    "has_nurs",
    "form",
    "children",
    "housing",
    "finance",
    "social",
    "health",
    "class",
]
nursery = pd.read_csv("../../nursery.data", names=cols)
nursery["children"] = pd.to_numeric(nursery["children"], errors="coerce")
print(
    "Mean 'children' grouped by 'finance':\n",
    nursery.groupby("finance")["children"].mean(),
)
