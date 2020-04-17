from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.3* (x-5)**2 + 1
y2 = 1.5 * x + 3
y3 = np.sin(x)**2
y4 = 10 * np.exp(-x) + 1

# 창1개에 여러개의 그래프 출력
# 2x2 모양으로 출
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.plot(x,y1)

plt.subplot(2,2,2)
plt.plot(x,y2)

plt.subplot(2,2,3)
plt.plot(x,y3)

plt.subplot(2,2,4)
plt.plot(x,y4)
