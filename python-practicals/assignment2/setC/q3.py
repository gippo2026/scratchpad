import numpy as np

a1 = np.array([0, 1, 3])
a2 = np.array([2, 4, 5])
print("Original array1:", a1)
print("Original array2:", a2)
print("Cross-correlation of the said arrays:\n", np.cov(a1, a2))
