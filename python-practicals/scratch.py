import inspect

import matplotlib.pyplot as plt  # import whatever library you need

print(inspect.signature(plt.scatter))
print(plt.scatter.__doc__)
