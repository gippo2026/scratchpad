import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import show_plot

iris = pd.read_csv("../../Iris.csv")

# Q1. Relationship between petal length and petal width
plt.plot(iris["PetalLengthCm"], iris["PetalWidthCm"], "o")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal length vs petal width")
plt.show()

# Q2. Scatter plots to compare two features of iris
plt.scatter(iris["SepalLengthCm"], iris["SepalWidthCm"])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter plot: sepal length vs sepal width")
plt.show()

# Q3. Box plots of each feature across the three species
for col in ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]:
    sns.boxplot(x="Species", y=col, data=iris)
    plt.title("Box plot: " + col + " by species")
    plt.show()

# Q4. Histogram for Sepal Length
plt.hist(iris["SepalLengthCm"], bins=15, edgecolor="k")
plt.title("Histogram of sepal length")
plt.show()

# Q5. Correlation matrix using a heatmap
num = iris.select_dtypes(include="number")
sns.heatmap(num.corr(), annot=True)
plt.title("Correlation matrix heatmap")
plt.show()
