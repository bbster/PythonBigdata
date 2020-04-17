from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()

# x축, y축, 제목, 격자 그리기
plt.plot(x,y1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Graph')
plt.grid(True)
plt.show()

# 범례 출력
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.legend(['data1', 'data2', 'data3', 'data4'])
plt.show()

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.legend(['y=x', 'y=x+1', 'y=x+2', 'y=x+3'])
plt.show()

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.legend(['y=x', 'y=x+1', 'y=x+2', 'y=x+3'], loc='lower right')
plt.show()
