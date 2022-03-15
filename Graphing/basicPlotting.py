# Tom Simpson
# Learning matplotlib
# 25/07/21


# Imoporting Modules
import matplotlib.pyplot as plt
import numpy as np

# Generating line
xpoints = np.array([0, 10])
ypoints = np.array([0, 10])
plt.plot(xpoints, ypoints, marker = '*')

# Plotting a points
xpoints = np.array([10, 0])
ypoints = np.array([0, 10])
plt.plot(xpoints, ypoints, "bo")


# Showing plot
plt.show()
