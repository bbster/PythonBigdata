import numpy as np

data1 = 'people', 'boy', 'girl', 'man', 'woman'
data2 = '1.5', '2.5', '3.5', '4.5'
data3 = '10', '20', '30', '40'

arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

print(arr1)
print(arr2)
print(arr3)
print('-'*40)

print(type(arr1))
print(type(arr2))
print(type(arr3))
print('-'*40)

print(arr1.dtype)  # <U6 U: 유니코드 6: 배열내 가장긴 문자열 길이
print(arr2.dtype)  # <U3 
print(arr3.dtype)  # <U2
print('-'*40)

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print('-'*40)

# numpy 배열의 형변환 : astype
arr_f = arr2.astype(float)
print(arr_f)
print(arr_f.dtype)
print('-'*40)

arr_f = arr3.astype(int)
print(arr_f)
print(arr_f.dtype)
print('-'*40)

arr_f = arr1.astype(str)
print(arr_f)
print(arr_f.dtype)
print('-'*40)

arr_f = arr1.astype(object)
print(arr_f)
print(arr_f.dtype)
print('-'*40)
