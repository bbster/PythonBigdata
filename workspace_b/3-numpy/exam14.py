import numpy as np

data1 = 10,20,30,40,50,60

# numpy 1차원 배열
arr1 = np.array(data1)
print(arr1)
print('-'*40)

# 1차원 슬라이싱
print(arr1[1:4])
print(arr1[1:])
print(arr1[:4])
print('-'*40)

arr1[2:5] = 35,45,55  # 부분값 변경 / 2~4번째 항목
print(arr1)
print('-'*40)

arr1[2:5] = 37  # 부분값 변경 / 2~4번째 항목 모두 37로
print(arr1)
print('-'*40)

# 2차원 배열
arr2 = np.arange(10, 100, 10).reshape(3, 3)
print(arr2)
print('-'*40)

# 2차원 슬라이싱
# 배열명[행시작:행끝, 열시작:열끝]
print(arr2[1:3, 1:3])
print('-'*40)

# 배열명[행위치][열시작:열끝]
print(arr2[1][1:3])
print('-'*40)

# 부분값 변경
# 배열명[행위치:행끝,열시작:열끝]
print(arr2)
print('-'*40)
arr2[0:2, 1:3] = [[25,35],[55,65]]
print(arr2)
print('-'*40)
