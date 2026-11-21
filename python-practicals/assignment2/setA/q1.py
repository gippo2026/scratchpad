import numpy as np

arr = np.array([[0, 1], [2, 3]])
flat = arr.flatten()

print("\nOriginal array: \n", arr)
print("\nMaximum: ", flat.max())
print("\nMinimum: ", flat.min())
