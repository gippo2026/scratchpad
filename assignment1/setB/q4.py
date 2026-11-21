import pandas as pd

hwData = pd.read_csv("../../heightweight.csv")

print("Number of observations: ", len(hwData))
print("\nMissing values: ", hwData.isnull().sum().sum())
print("\nNot a number values: ", hwData.isna().sum().sum())
