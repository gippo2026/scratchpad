import pandas as pd

hwData = pd.read_csv("../../heightweight.csv")

print("\nFirst 10 rows: \n", hwData.head(10))
print("\nLast 10 rows: \n", hwData.tail(10))
print("\nRandom 20 rows: \n", hwData.sample(20))
