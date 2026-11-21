import numpy as np

a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
w = np.array([1, 2, 2])
print("Original flattened array:\n", a)
print("Weighted average along axis 1:\n", np.average(a, axis=1, weights=w))
