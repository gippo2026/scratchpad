import pandas as pd

data = pd.read_csv("../../data.csv")
print("Before replacing the missing values: \n", data)

data["salary"] = data["salary"].fillna(data["salary"].mean())
data["age"] = data["age"].fillna(data["age"].mean())

print("\nAfter replacing the missing values with mean: \n", data)
