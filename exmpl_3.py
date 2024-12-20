# exmpl 3

# Plotting using numpy objects

import matplotlib.pyplot as plt
from numpy import arange

X = arange(0,6,0.01) # similar to range in exmpl 2 but can handle floats
Y = [x**2 for x in X]

plt.plot(X,Y)
plt.show()
