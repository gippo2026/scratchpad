import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, Binarizer

# Q1

wineData = pd.read_csv("../../winequality-red.csv", sep=";")

# q2

print(
    "Minmax Scaled: \n",
    pd.DataFrame(
        MinMaxScaler().fit_transform(wineData), columns=wineData.columns
    ).head(),
)

# q3

print(
    "\nStandardized : \n",
    pd.DataFrame(
        StandardScaler().fit_transform(wineData), columns=wineData.columns
    ).head(),
)

# q4

print(
    "\nNormalized: \n",
    pd.DataFrame(Normalizer().fit_transform(wineData), columns=wineData.columns).head(),
)

# q5

print(
    "\nBinarized: \n",
    pd.DataFrame(
        Binarizer(threshold=5).fit_transform(wineData), columns=wineData.columns
    ).head(),
)
