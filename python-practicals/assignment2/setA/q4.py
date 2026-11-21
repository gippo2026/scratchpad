import numpy as np

points = np.array([[1, 2], [3, 4], [5, 6]])
total = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        total += np.sum(np.abs(points[i] - points[j]))

print("Sum of manhattan distances: ", total)
