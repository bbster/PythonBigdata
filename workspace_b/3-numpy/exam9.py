import numpy as np

# 0<=난수<1 사이의 실수 난수 1개 생성
f1 = np.random.rand()
print(f1)
print(type(f1))
print('-'*40)

arr1 = np.random.rand(2,3)  # 2*3 배열
print(arr1)
print(type(arr1))
print('-'*40)

arr2 = np.random.rand(2,3,4)  # 2*3*4 배열
print(arr2)
print(type(arr2))
print('-'*40)

#  1~29 사이의 정수 난수 1개 생성
n1 = np.random.randint(1,30)
print(n1)
print(type(n1))
print('-'*40)

#  행렬의 크기 지정
n2 = np.random.randint(1,30, size=(3,4))
print(n2)
print(type(n2))
print('-'*40)
