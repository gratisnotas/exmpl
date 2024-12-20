# exmpl 4

# multiple plots

import matplotlib.pyplot as plt

X = range(1,5)
Y1 = [x**2 for x in X]
Y2 = [x*3 for x in X]
Y3 = [x*4 for x in X]

print(Y3)

plt.plot(X, Y1, X, Y2, X, Y3) # same X different Y
plt.show()
