import pandas as pd

data = pd.read_csv("../../data.csv")

print("Basic statistical data: \n", data.describe())
print("\nShape of Data: ", data.shape)
print("\nFirst 3 rows: \n", data.head(3))
