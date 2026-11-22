import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import show_plot

iris = pd.read_csv("../../Iris.csv")

# Q1. Random array of 50 integers - line, scatter, histogram and box plot
x = np.random.randint(0, 100, 50)

plt.plot(x, color="g", marker="o", label="data")
plt.xlabel("index")
plt.ylabel("value")
plt.title("Line chart of 50 random integers")
plt.legend()
plt.show()

plt.scatter(x, range(50), color="b", alpha=0.7)
plt.title("Scatter plot of 50 random integers")
plt.show()

plt.hist(x, bins=10, color="y", edgecolor="k")
plt.title("Histogram of 50 random integers")
plt.show()

plt.boxplot(x)
plt.title("Box plot of 50 random integers")
plt.show()

# Q2. Add two outliers and display the box plot
x = np.append(x, [500, -200])
plt.boxplot(x)
plt.title("Box plot after adding two outliers")
plt.show()

# Q3. Subject names and marks - pie chart and bar chart
subjects = ["Math", "English", "Science", "History", "Computer"]
marks = [80, 75, 90, 65, 85]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Pie chart of marks by subject")
plt.show()

plt.bar(subjects, marks, color="g")
plt.title("Bar chart of marks by subject")
plt.show()

# Q4. Bar plot of frequency of the three iris species
iris["Species"].value_counts().plot(kind="bar")
plt.title("Bar plot: frequency of iris species")
plt.show()

# Q5. Pie plot of frequency of the three iris species
iris["Species"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Pie plot: frequency of iris species")
plt.show()
