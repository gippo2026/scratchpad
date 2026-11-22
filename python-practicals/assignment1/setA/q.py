import matplotlib.pyplot as plt
import pandas as pd

import show_plot

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
print("Dataframe:\n", df)

# Q2. Shape, rows-columns, data types, feature names, description
print("Shape (rows, columns):", df.shape)
print("Data types:\n", df.dtypes)
print("Feature names:", list(df.columns))
print("Description:\n", df.describe())

# Q3. Basic statistical details
print("Basic statistical details:\n", df.describe())

# Q4. Add 5 rows with duplicate / missing values, add empty 'remarks' column
df.loc[10] = ["Amit", 20, 82]  # duplicate
df.loc[11] = ["Ravi", None, 88]  # missing
df.loc[12] = ["Neha", 21, None]
df.loc[13] = [None, None, None]
df.loc[14] = ["Sita", 22, 91]
df["remarks"] = None
print("After adding duplicate/missing rows and 'remarks' column:\n", df)

# Q5. Number of observations, missing values, duplicate values
print("Number of observations:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# Q6. Drop 'remarks' column and all null/empty rows
df = df.drop(columns="remarks").dropna()
print("After dropping 'remarks' and null rows:\n", df)

# Q7. Line plot of name vs percentage
plt.plot(df["name"], df["percentage"], color="g", marker="o")
plt.xlabel("name")
plt.ylabel("percentage")
plt.title("Line plot: name vs percentage")
plt.show()

# Q8. Scatter plot of name vs percentage
plt.scatter(df["name"], df["percentage"])
plt.xlabel("name")
plt.ylabel("percentage")
plt.title("Scatter plot: name vs percentage")
plt.show()
