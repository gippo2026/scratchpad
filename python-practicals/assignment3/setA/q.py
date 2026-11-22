import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("../../data.csv").rename(columns=str.title)

# Q1. Describe, shape, first 3 rows
print("Description:\n", df.describe())
print("Shape:", df.shape)
print("First 3 rows:\n", df.head(3))

# Q2. Replace missing Salary and Age with column mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Q3a. One-Hot encode Country
ohe = OneHotEncoder(handle_unknown="ignore")
country = pd.DataFrame(ohe.fit_transform(df[["Country"]]).toarray())
df = pd.concat([df, country], axis=1).drop(columns="Country")

# Q3b. Label encode Purchased
df["Purchased"] = LabelEncoder().fit_transform(df["Purchased"])
print("Dataframe after filling nulls and encoding:\n", df)
