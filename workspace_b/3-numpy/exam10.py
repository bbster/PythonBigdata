import numpy as np

data1 = 10,20,30,40,50
data2 = 100,200,300,400,500

arr1 = np.array(data1)
arr2 = np.array(data2)

print(arr1)
print(arr2)
print('-'*40)

# numpy 배열을 통째로 게산
arr_add = arr1 + arr2
print(arr_add)
print('-'*40)

arr_add = arr1 - arr2
print(arr_add)
print('-'*40)

arr_add = arr1 * arr2
print(arr_add)
print('-'*40)

arr_add = arr1 / arr2
print(arr_add)
print('-'*40)

arr_add = arr1 + 7
print(arr_add)
print('-'*40)

arr_add = arr1 ** 2
print(arr_add)
print('-'*40)
