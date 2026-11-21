import pandas as pd

# Q1. Dataframe with name, age, percentage - 10 rows (dictionary method)
data = {
    "name": [
        "Amit",
        "Neha",
        "Ravi",
        "Sita",
        "Karan",
        "Meera",
        "Rahul",
        "Priya",
        "Ajay",
        "Kavya",
    ],
    "age": [20, 21, 19, 22, 20, 21, 23, 20, 19, 22],
    "percentage": [82, 75, 88, 91, 67, 73, 85, 79, 60, 95],
}
df = pd.DataFrame(data)

# 03 Basic Statistical data

print("basic statistical data: \n", df.describe())
