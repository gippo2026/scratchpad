import pandas as pd
from scipy.stats import gmean, hmean

marks = pd.DataFrame({
    "Math":     [80, 75, 90, 60, 85, 70, 95, 65, 88, 72],
    "English":  [70, 80, 65, 75, 60, 85, 90, 72, 68, 78],
    "Science":  [85, 60, 78, 88, 92, 66, 74, 80, 70, 84],
    "History":  [65, 72, 80, 68, 75, 88, 60, 90, 78, 82],
    "Computer": [90, 85, 70, 95, 80, 75, 88, 62, 72, 86],
})

print("Arithmetic mean:\n", marks.mean())
print("Geometric mean:\n", gmean(marks))
print("Harmonic mean:\n", hmean(marks))
