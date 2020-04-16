### NUMPY

## 1차원 배열 생성
```python
#  1차원 배열

import numpy as np

data1 = [1, 2, 3, 4, 5]
data2 = [1.1, 2.2, 3, 4.4, 5.5]
data3 = 1,2,3,4,5
data4 = 'string', 'string2'
data5 = ['string', 1, ['string2', 'string3']]

#  numpy 1차원 배열 생성

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

''' 
결과값
arr1 :  [1 2 3 4 5]
arr2 :  [1.1 2.2 3.  4.4 5.5]
arr3 :  [1 2 3 4 5]
arr4 :  ['string' 'string2']
arr5 :  ['string' 1 list(['string2', 'string3'])]
----------------------------------------
<class 'numpy.ndarray'>
<class 'numpy.ndarray'>
<class 'numpy.ndarray'>
<class 'numpy.ndarray'>
<class 'numpy.ndarray'>
----------------------------------------
int32
float64
int32
<U7
object
'''
```
## 2차원 배열 생성
```python
2차원 배열 생성 
import numpy as np

data1 = 1,2,3
data2 = 4,5,6
data3 = 7,8,9


arr1 = np.array([data1, data2, data3])

print(arr1)
print('-'*40)

'''
결과
[[1.  2.  3. ]
 [4.  5.5 6. ]
 [7.  8.  9. ]]
----------------------------------------
<class 'numpy.ndarray'>
float64
'''
```
## arange() numpy 배열 생성하기
```python
import numpy as np

arr1 = np.arange(0, 10, 2)

print(arr1)
print(type(arr1))
print(arr1.dtype)
print('-'*40)

arr2 = np.arange(0, 10)

print(arr2)
print(type(arr2))
print(arr2.dtype)
print('-'*40)

arr3 = np.arange(5)

print(arr3)
print(type(arr3))
print(arr3.dtype)
print('-'*40)

'''
결과값
[0 2 4 6 8]
<class 'numpy.ndarray'>
int32
----------------------------------------
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
int32
----------------------------------------
[0 1 2 3 4]
<class 'numpy.ndarray'>
int32
'''
```
## numpy reshape(m,n)
```python
import numpy as np

arr1 = np.arange(1, 13).reshape(4,3)  # reshape(행(세로), 열(가로))
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)

'''
결과값
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
<class 'numpy.ndarray'>
int32
(4, 3)

데이터가 행,열이 맞지 않으면 에러발생
'''
```
## numpy linspace()
 - linspace()로 만들어진 데이터는 모두 실수로 생성됨
```python
import numpy as np

arr1 = np.linspace(1, 5, 10)  # 1~5 사이의 10개 데이터 생성

print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print('-'*40)

arr2 = np.linspace(1, 10, 10)  # 1~5 사이의 10개 데이터 생성

print(arr2)
print(type(arr2))
print(arr2.dtype)
print(arr2.shape)
print('-'*40)

arr3 = np.linspace(1, np.pi, 20)  # 1~5 사이의 10개 데이터 생성

print(arr3)
print(type(arr3))
print(arr3.dtype)
print(arr3.shape)
print('-'*40)

'''
결과값
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
<class 'numpy.ndarray'>
float64
(10,)
----------------------------------------
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
<class 'numpy.ndarray'>
float64
(10,)
----------------------------------------
[1.         1.1127154  1.22543081 1.33814621 1.45086161 1.56357701
 1.67629242 1.78900782 1.90172322 2.01443863 2.12715403 2.23986943
 2.35258483 2.46530024 2.57801564 2.69073104 2.80344645 2.91616185
 3.02887725 3.14159265]
<class 'numpy.ndarray'>
float64
(20,)
'''
```
## numpy zeros, ones
```python
import numpy as np

arr1 = np.zeros(10)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print('-'*40)

arr1 = np.zeros((3, 4))
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print('-'*40)

arr1 = np.ones(10)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print('-'*40)

arr1 = np.ones((3, 4))
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print('-'*40)

'''
결과값
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
<class 'numpy.ndarray'>
float64
(10,)
----------------------------------------
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
<class 'numpy.ndarray'>
float64
(3, 4)
----------------------------------------
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
<class 'numpy.ndarray'>
float64
(10,)
----------------------------------------
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
<class 'numpy.ndarray'>
float64
(3, 4)
'''
```
##  단위 행렬 생성
```python
import numpy as np

#  단위 행렬 생성
arr1 = np.eye(3)
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print('-'*40)

'''
결과값
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
<class 'numpy.ndarray'>
float64
(3, 3)
```
## numpy 배열의 형 변환 
```python
import numpy as np

data1 = 'people', 'boy', 'girl', 'man', 'woman'
data2 = '1.5', '2.5', '3.5', '4.5'
data3 = '10', '20', '30', '40'

arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

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
'''
결과값
[1.5 2.5 3.5 4.5]
float64
----------------------------------------
[10 20 30 40]
int32
----------------------------------------
['people' 'boy' 'girl' 'man' 'woman']
<U6
----------------------------------------
['people' 'boy' 'girl' 'man' 'woman']
object
----------------------------------------

'''

```