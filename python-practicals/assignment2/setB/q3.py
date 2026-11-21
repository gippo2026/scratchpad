import pandas as pd

iris = pd.read_csv("Iris.csv")
num = iris.select_dtypes(include="number")
print("Column-wise mean:\n", num.mean())
print("Column-wise median:\n", num.median())
