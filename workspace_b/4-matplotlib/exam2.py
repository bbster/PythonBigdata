from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-4.5,5,0.5)
y = 2 * x**2

print([x,y])

plt.plot(x,y)
plt.show()
