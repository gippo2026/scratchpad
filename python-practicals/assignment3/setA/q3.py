import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

data = pd.read_csv("../../data.csv")

data["salary"] = data["salary"].fillna(data["salary"].mean())
data["age"] = data["age"].fillna(data["age"].mean())

ohe = OneHotEncoder(handle_unknown="ignore")
country = pd.DataFrame(ohe.fit_transform(data[["country"]]).toarray())
data = pd.concat([data, country], axis=1).drop(columns="country")

data["purchased"] = LabelEncoder().fit_transform(data["purchased"])

print("Dataframe after encoding:\n", data)
