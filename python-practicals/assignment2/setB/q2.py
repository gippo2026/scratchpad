import pandas as pd

iris = pd.read_csv("Iris.csv")
print("Records per species:\n", iris["Species"].value_counts())
