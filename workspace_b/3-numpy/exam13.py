import numpy as np

data1 = 10,20,30,40,50,60

arr1 = np.array(data1)
print(arr1)
print('-'*40)

# 1차원 인덱싱
arr1 = np.array(data1)
print(arr1[2])
print(arr1[[1,3,5]])
print(arr1[arr1 > 40])
#print(data1[data1 > 40]) # list는 인덱싱에 조건 달수없음
print('-'*40+'1차원 끝')

# 2차원 인덱싱 
arr2 = np.arange(10, 100, 10).reshape(3, 3)
print(arr2[0,2], ' - arr2[0,2]')
arr2[0,2] = 35
print(arr2, ' - arr2[0,2] 자리에 35값 넣음')
arr2[0][2] = 55
print(arr2, ' - arr2[0][2] 자리에 55값 넣음')
print('-'*40+'인덱싱한 배열값')
print(arr2[arr2 > 40])
print('-'*40+'2차원 끝')

# 1개 행 
# 전부 변경 : 배열
arr2[1] = np.array([45,55,66])
print(arr2)
print('-'*40)

# 1개 행 전부 변경 : 리스트
arr2[2] = [145,155,166]
print(arr2)
print('-'*40)

# 2차원 배열에서 특정위치값 여러개 선택
# 배열명[[행위치], [열위치]]
print(arr2[[0,2],[0,1]])  # [0,0],[2,1]
