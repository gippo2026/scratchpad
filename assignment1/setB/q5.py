import pandas as pd

hwData = pd.read_csv("../../heightweight.csv")
print("Original dataframe: \n", hwData)

hwData["BMI"] = hwData["Height(Inches)"] / hwData["Weight(Pounds)"] ** 2
print("\nDataframe with BMI: \n", hwData)
