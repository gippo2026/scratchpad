import matplotlib.pyplot as plt
import numpy as np

import show_plot

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

# np.histogram only computes counts and bin edges -- it does not draw anything.
counts, edges = np.histogram(nums, bins)
print("Histogram counts: ", counts)
print("Bin edges: ", edges)

# plt.hist creates the figure; show_plot's patched plt.show() saves it.
plt.hist(nums, bins=bins.tolist(), edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
