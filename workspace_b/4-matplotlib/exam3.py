from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-4,5,2)
y1 = 5 * x +30
y2 = 2 * x**2 
y3 = 4 * x**2 + 10

plt.plot(x,y1, x,y2,x,y3)

plt.show()
