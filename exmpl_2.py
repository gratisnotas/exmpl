# exmpl 2

# This eample plots a parabola using both x and y axis

import matplotlib.pyplot as plt

x = range(6)
y = [i**2 for i in x]

plt.plot(x,y)
plt.show()

# The output would be the same if just x is plotted
