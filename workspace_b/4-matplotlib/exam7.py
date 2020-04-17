from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4= x + 3

plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()

# 선 색상 지정 : magenta, yellow, black, cyan
plt.plot(x,y1,'m', x,y2,'y', x,y3,'b', x,y4,'c')
plt.show()

# 선 스타일 지정 : 실선, 파선, 점선, 파선 점선 혼합
plt.plot(x,y1,'-', x,y2,'--', x,y3,':', x,y4,'-.')
plt.show()

# 마커 지정 : 원, 삼각형, 사각형, 다이아몬드 
plt.plot(x,y1,'o', x,y2,'^', x,y3,'s', x,y4,'d')
plt.show()

# 선 색상, 스타일, 마터를 혼합해서 지정
plt.plot(x,y1,'m-o', x,y2,'y--^', x,y3,'b:s', x,y4,'c-.d')
plt.show()
