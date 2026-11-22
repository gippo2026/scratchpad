import matplotlib.pyplot as plt
import pandas as pd

import show_plot

# Q1. Load dataset and print first 10, last 10 and random 20 rows
hw = pd.read_csv("../../heightweight.csv").rename(
    columns={"Height(Inches)": "Height", "Weight(Pounds)": "Weight"}
)
print("First 10 rows:\n", hw.head(10))
print("Last 10 rows:\n", hw.tail(10))
print("Random 20 rows:\n", hw.sample(20))

# Q2. Shape, size, datatypes
print("Shape:", hw.shape)
print("Size:", hw.size)
print("Data types:\n", hw.dtypes)

# Q3. Basic statistical details
print("Basic statistical details:\n", hw.describe())

# Q4. Number of observations, missing values and NaN values
print("Number of observations:", len(hw))
print("Missing values:", hw.isnull().sum().sum())
print("NaN values:", hw.isna().sum().sum())

# Q5. Add BMI column = weight / height^2
hw["BMI"] = hw["Weight"] / hw["Height"] ** 2
print("Dataframe with BMI column:\n", hw)

# Q6. Maximum and minimum BMI
print("Maximum BMI:", hw["BMI"].max())
print("Minimum BMI:", hw["BMI"].min())

# Q7. Scatter plot of height vs weight
plt.scatter(hw["Height"], hw["Weight"])
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter plot: height vs weight")
plt.show()
