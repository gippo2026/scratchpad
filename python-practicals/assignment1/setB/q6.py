import pandas as pd

hwData = pd.read_csv("../../heightweight.csv")
hwData["BMI"] = hwData["Height(Inches)"] / hwData["Weight(Pounds)"] ** 2

print("Minimum BMI: ", hwData["BMI"].max())
print("Maximum BMI: ", hwData["BMI"].min())
