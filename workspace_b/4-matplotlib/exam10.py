from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

height = 165,177,160,180,185,155,172
weight = 62,27,55,74,90,43,64

plt.scatter(height, weight)
plt.xlabel('Height(cm)')
plt.ylabel('Weight(kg)')
plt.title('Height & Weight')
plt.grid(True)
plt.show()

# 원의 크기와 색상 지정
plt.scatter(height, weight, s=50, c='r')
plt.xlabel('Height(cm)')
plt.ylabel('Weight(kg)')
plt.title('Height & Weight')
plt.grid(True)
plt.show()

# 데이터별로 마커의 크기와 색상 지정
# size = 100 * np.arange(1, 8)
size = 100, 200, 300, 400, 500, 600, 700
colors = 'r', 'g', 'b', 'c', 'm', 'k', 'y'

plt.scatter(height,weight, s=size, c=colors)
plt.show()