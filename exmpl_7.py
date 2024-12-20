# exmpl 7

# setting labels for x- and y-axis

import matplotlib.pyplot as plt
from numpy import arange

X = arange(1,7,1)
Y = X**2

plt.xlabel('x values')
plt.ylabel('y values')
plt.plot(X,Y)
plt.show()
