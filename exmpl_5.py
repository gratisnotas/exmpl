# exmpl 5

# adding grid lines to plot

import matplotlib.pyplot as plt
from numpy import arange

X = arange(1,5,0.1)
Y = pow(X,0.5)

plt.grid(True)
plt.plot(X,Y)
plt.show()
