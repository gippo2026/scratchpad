import pandas as pd

iris = pd.read_csv("Iris.csv")
sample = iris.sample(10)
print("10 random samples:\n", sample)

sample_num = sample.select_dtypes(include="number")
print("Maximum values:\n", sample_num.max())
print("Minimum values:\n", sample_num.min())
