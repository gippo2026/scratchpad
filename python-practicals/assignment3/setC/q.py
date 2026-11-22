import pandas as pd

# Q1. Import libraries and load dataset into a pandas dataframe
stu = pd.read_csv("../../student_bucketing.csv").rename(columns={"marks": "Marks"})

# Q2. Display first five rows
print("First five rows:\n", stu.head())

# Q3. Discretize marks into 5 buckets using cut() and display top 10 rows
labels = ["Poor", "Below_average", "Average", "Above_average", "Excellent"]
stu["grade"] = pd.cut(stu["Marks"], bins=5, labels=labels)
print("Top 10 rows with 'grade' buckets:\n", stu.head(10))
