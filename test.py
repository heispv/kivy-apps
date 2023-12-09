import numpy as np
import matplotlib.pyplot as plt

# generate random data as X, Y
X = np.random.rand(100, 1)
Y = np.random.rand(100, 1)

# plot the data
plt.scatter(X, Y)
plt.show()
