from matplotlib import pyplot as plt
import numpy as np

data1 = 30,44,10,70,25
data2 = 10,20,30,40,50

# 리스트 내용을 그래프로 출
plt.plot(data1)
plt.show()

# numpy 배열 이용
arr = np.array(data2)
plt.plot(arr)
plt.show()

# x축 y축 값 지정
# plot(x,y)
plt.plot([1,2,3,4,5], data1)
plt.show()
