import numpy as np

data1 = [1, 2, 3, 4, 5]
data2 = [1.1, 2.2, 3, 4.4, 5.5]
data3 = 1,2,3,4,5
data4 = 'string', 'string2'
data5 = ['string', 1, ['string2', 'string3']]

#  numpy 1차원 배열 생

arr1 = np.array(data1)
arr2 = np.array(data2)  # 정수와 실수가 섞여있으면, 모두 실수로 변환
arr3 = np.array(data3)
arr4 = np.array(data4)
arr5 = np.array(data5)

print('arr1 : ', arr1)
print('arr2 : ', arr2)
print('arr3 : ', arr3)
print('arr4 : ', arr4)
print('arr5 : ', arr5)
print('-'*40)


print(type(arr1))  # 변수에 저장된 데이터 타입
print(type(arr2))
print(type(arr3))
print(type(arr4))
print(type(arr5))
print('-'*40)

print(arr1.dtype)  # numpy 배열에 저장된 데이터 종류
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)