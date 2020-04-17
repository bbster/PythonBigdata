from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.xlabel('x-축')
plt.ylabel('y-축')
plt.title('선그리기')
plt.grid(True)
plt.legend(['데이터1', '데이터2', '데이터3', '데이터4',])
plt.show()

# 한글 설정
mpl.rcParams['font.family'] = 'Malgun Gothic'

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.xlabel('x-축')
plt.ylabel('y-축')
plt.title('선그리기')
plt.grid(True)
plt.legend(['데이터1', '데이터2', '데이터3', '데이터4'])
plt.show()

# 특정위치에 문자열 위치
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.text(0, 6, '데이터1')
plt.text(0, 5, '데이터2')
plt.text(3, 1, '데이터3')
plt.text(3, 0, '데이터4')
plt.show()
