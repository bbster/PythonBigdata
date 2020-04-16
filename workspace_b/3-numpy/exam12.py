import numpy as np

data1 = 1,2,3,4
data2 = 10,20,30,40

arr1 = np.array(data1).reshape(2,2)
arr2 = np.array(data2).reshape(2,2)

print(arr1)
print(arr2)
print('-'*40)

# 행렬 연산
arr_dot = np.dot(arr1, arr2)  # 행렬 곱 
print(arr_dot)
print('-'*40)

arr_transpose = np.transpose(arr1)  # 전치 행렬 / 행과 열을 바꿈
print(arr1)
print(arr_transpose)
print('-'*40)

arr_inv = np.linalg.inv(arr1)  # 역 행렬
print(arr1)
print(arr_inv)
print('-'*40)

arr_det = np.linalg.det(arr1)  # 행렬식
print(arr1)
print(arr_det)
print('-'*40)
