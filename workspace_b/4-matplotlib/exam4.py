from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-4.5,5,0.5)
y1 = 5 * x +30
y2 = 2 * x**2 
y3 = 4 * x**2 + 10

plt.figure(1)  # 그래프창을 생성, 창번호 부여
plt.plot(x, y1, x, y2)

plt.figure(2)
plt.plot(x, y2)

plt.figure(3)
plt.plot(x, y1, x, y2, x, y3)
