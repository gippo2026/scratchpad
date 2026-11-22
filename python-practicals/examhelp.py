import inspect

import matplotlib.pyplot as plt

print(inspect.signature(plt.hist))
print(plt.hist.__doc__[:1000])
