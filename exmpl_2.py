# exmpl 2

# This eample plots a parabola using both x and y axis

import matplotlib.pyplot as plt

X = range(6)
Y = [x**2 for x in X]

plt.plot(X,Y)
plt.show()

# The output would be the same if just x is plotted
