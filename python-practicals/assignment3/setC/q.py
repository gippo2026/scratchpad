import pandas as pd

# q1

studentData = pd.read_csv("../../student_bucketing.csv")

# q2

print("First 5 records: \n", studentData.head())

# q3

labels = ["Poor", "Below_average", "Average", "Above_average", "Excellent"]
studentData["grade"] = pd.cut(studentData["marks"], bins=5, labels=labels)
print("\nTop 10 rows with grade bucket:\n", studentData.head(10))
