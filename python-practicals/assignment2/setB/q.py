import pandas as pd
from scipy.stats import gmean, hmean

# Q1. Read iris csv, take samples, display max/min of all numeric attributes
iris = pd.read_csv("../../Iris.csv")
sample = iris.sample(10)
print("10 random samples:\n", sample)
sample_num = sample.select_dtypes(include="number")
print("Maximum values:\n", sample_num.max())
print("Minimum values:\n", sample_num.min())

# Q2. Number of records for each distinct value of class attribute (entire dataset)
print("Records per species:\n", iris["Species"].value_counts())

# Q3. Column-wise mean and median
num = iris.select_dtypes(include="number")
print("Column-wise mean:\n", num.mean())
print("Column-wise median:\n", num.median())

# Q4. Shape, data types and statistical summary
print("Shape:", iris.shape)
print("Data types:\n", iris.dtypes)
print("Statistical summary:\n", iris.describe())

# Q5. Dataframe of 5 subjects and marks of 10 students - AM, GM, HM
marks = pd.DataFrame(
    {
        "Math": [80, 75, 90, 60, 85, 70, 95, 65, 88, 72],
        "English": [70, 80, 65, 75, 60, 85, 90, 72, 68, 78],
        "Science": [85, 60, 78, 88, 92, 66, 74, 80, 70, 84],
        "History": [65, 72, 80, 68, 75, 88, 60, 90, 78, 82],
        "Computer": [90, 85, 70, 95, 80, 75, 88, 62, 72, 86],
    }
)
print("Arithmetic mean:\n", marks.mean())
print("Geometric mean:\n", gmean(marks))
print("Harmonic mean:\n", hmean(marks))
