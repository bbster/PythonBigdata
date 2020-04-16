from matplotlib import pyplot as plt
import numpy as np

data1 = 10,14,19,20,25

# 리스트 내용을 그래프로 출
plt.plot(data1)
plt.show()

# numpy 배열 이용
arr = np.array(data1)
plt.plot(arr)
plt.show()
