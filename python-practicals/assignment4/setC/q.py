import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import show_plot

iris = pd.read_csv("../../Iris.csv")

# Q1. Pairplot - check which species seems most separable
sns.pairplot(iris, hue="Species")
plt.show()
# Observation: Iris-setosa is the most separable species

# Q2. Box plot showing IQR and outliers for three species for each feature
for col in ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]:
    sns.boxplot(x="Species", y=col, data=iris)
    plt.title("IQR and outliers: " + col + " by species")
    plt.show()

# Q3. Joint plot using "kde" between Sepal length and Sepal width
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, kind="kde")
plt.show()

# Q4. Histogram of the three species of iris
sns.histplot(data=iris, x="SepalLengthCm", hue="Species", multiple="stack")
plt.title("Histogram of sepal length by species")
plt.show()
