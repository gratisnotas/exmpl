# exmpl 6

# handling axis

import matplotlib.pyplot as plt
from numpy import arange

X = arange(1,5,0.5)
Y = X*1.5

plt.axis([-1,6,-5,20]) # setting x- and y-axis limits in the plot
plt.grid(True)
plt.plot(X,Y)
plt.show()

# plt.xlim([x_min,x_max]) and  plt.ylim([y_min,y_max]) can also be used
