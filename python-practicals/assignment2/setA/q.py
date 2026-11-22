import numpy as np
import pandas as pd

# Q1. Maximum and minimum value of a given flattened array
arr = np.array([[0, 1], [2, 3]])
flat = arr.flatten()
print("Original flattened array:\n", arr)
print("Maximum value of the above flattened array:", flat.max())
print("Minimum value of the above flattened array:", flat.min())

# Q2. Euclidean distance between two data points using linalg.norm
pts = pd.DataFrame({"x": [1, 4], "y": [2, 5]})
print("Euclidean distance:", np.linalg.norm(pts.iloc[0].values - pts.iloc[1].values))

# Q3. Dataframe of data values - mean, range and IQR (dictionary method)
df = pd.DataFrame({"data": [13, 52, 44, 32, 30, 0, 36, 45]})
q1, q3 = df["data"].quantile([0.25, 0.75])
print("Mean:", df["data"].mean())
print("Range:", df["data"].max() - df["data"].min())
print("IQR:", q3 - q1)

# Q4. Sum of Manhattan distance between all pairs of points
points = np.array([[1, 2], [3, 4], [5, 6]])
total = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        total += np.sum(np.abs(points[i] - points[j]))
print("Sum of Manhattan distances:", total)

# Q5. Histogram of nums against bins
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums:", nums)
print("bins:", bins)
print("Result:", np.histogram(nums, bins))
