import pandas as pd

hwData = pd.read_csv("../../heightweight.csv")

print("Basic statistical details: \n", hwData.describe())
