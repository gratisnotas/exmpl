# exmpl 4

# multiple plots

import matplotlib.pyplot as plt
from numpy import array as ar

X = ar(range(1,5))
Y1 = X**2
Y2 = X*3
Y3 = X*4

plt.plot(X, Y1, X, Y2, X, Y3) # same X different Y
plt.show()
