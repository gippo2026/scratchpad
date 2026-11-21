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
print("Original DataFrame: \n", df)

# Q4. Add 5 rows with duplicate / missing values, add empty 'remarks' column
df.loc[10] = ["Amit", 20, 82]  # duplicate
df.loc[11] = ["Ravi", None, 88]  # missing
df.loc[12] = ["Neha", 21, None]
df.loc[13] = [None, None, None]
df.loc[14] = ["Sita", 22, 91]
df["remarks"] = None
print("\nAfter adding duplicate/missing rows and 'remarks' column:\n", df)
