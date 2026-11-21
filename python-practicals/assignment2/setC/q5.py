import pandas as pd

cols = ["parents", "has_nurs", "form", "children", "housing",
        "finance", "social", "health", "class"]
nursery = pd.read_csv("nursery.data", names=cols)
print("Mean 'children' grouped by 'finance':\n", nursery.groupby("finance")["children"].mean())
