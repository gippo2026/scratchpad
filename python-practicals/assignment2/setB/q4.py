import pandas as pd

iris = pd.read_csv("Iris.csv")
print("Shape:", iris.shape)
print("Data types:\n", iris.dtypes)
print("Statistical summary:\n", iris.describe())
