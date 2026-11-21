import pandas as pd

hwData = pd.read_csv("../../heightweight.csv")

print("Shape: \n", hwData.shape)
print("\nSize: \n", hwData.size)
print("\nDatatypes: \n", hwData.dtypes)
