import show_plot
import pandas as pd
import matplotlib.pyplot as plt

hwData = pd.read_csv("../../heightweight.csv")

plt.scatter(hwData["Height(Inches)"], hwData["Weight(Pounds)"], color="r", marker="+")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter plot height vs weight")
plt.show()
