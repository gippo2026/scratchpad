import numpy as np

p = np.array([1, 2, 3])
q = np.array([4, 6, 8])
r = 3
print("Minkowski distance:", np.sum(np.abs(p - q) ** r) ** (1 / r))
