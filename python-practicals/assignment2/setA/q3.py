import pandas as pd

df = pd.DataFrame({"data": [13, 45, 67, 23, 89, 65, 87, 32, 90]})
q1, q3 = df["data"].quantile([0.25, 0.75])

print("Mean: ", df.mean())
print("\nRange: ", df["data"].max() - df["data"].min())
print("\nIQR: ", q3 - q1)
