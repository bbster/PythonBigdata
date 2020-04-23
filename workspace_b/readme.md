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

'''
```

## 배열끼리 계산
```python
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

'''
결과값
[10 20 30 40 50]
[100 200 300 400 500]
----------------------------------------
[110 220 330 440 550]
----------------------------------------
[ -90 -180 -270 -360 -450]
----------------------------------------
[ 1000  4000  9000 16000 25000]
----------------------------------------
[0.1 0.1 0.1 0.1 0.1]
----------------------------------------
[17 27 37 47 57]
----------------------------------------
[ 100  400  900 1600 2500]
'''
```

## 배열 통계 연산
```python
import numpy as np

data1 = 10,20,30,40,50

arr1 = np.array(data1)
print(arr1)
print('-'*40)

arr_sum = arr1.sum()  # 합
print(arr_sum, type(arr_sum))
print('-'*40)

arr_mean = arr1.mean()  # 평균
print(arr_mean, type(arr_mean))
print('-'*40)

arr_std = arr1.std()  # 표준편차
print(arr_std, type(arr_std))
print('-'*40)

arr_var = arr1.var()  # 분산
print(arr_var, type(arr_var))
print('-'*40)

arr_max = arr1.max()  # 최대값
print(arr_max, type(arr_max))
print('-'*40)

arr_min = arr1.min()  # 최소
print(arr_min, type(arr_min))
print('-'*40)

arr_cumsum = arr1.cumsum()  # 누적 합
print(arr_cumsum, type(arr_cumsum))
print('-'*40)

arr_cumprod = arr1.cumprod()  # 누적 곱 
print(arr_cumprod, type(arr_cumprod))
print('-'*40)

'''
결과값
[10 20 30 40 50]
----------------------------------------
150 <class 'numpy.int32'>
----------------------------------------
30.0 <class 'numpy.float64'>
----------------------------------------
14.142135623730951 <class 'numpy.float64'>
----------------------------------------
200.0 <class 'numpy.float64'>
----------------------------------------
50 <class 'numpy.int32'>
----------------------------------------
10 <class 'numpy.int32'>
----------------------------------------
[ 10  30  60 100 150] <class 'numpy.ndarray'>
----------------------------------------
[      10      200     6000   240000 12000000] <class 'numpy.ndarray'>
'''
```
## 행렬 연산
```python
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
'''
결과값
[[1 2]
 [3 4]]
[[10 20]
 [30 40]]
----------------------------------------
[[ 70 100]
 [150 220]]
----------------------------------------
[[1 2]
 [3 4]]
[[1 3]
 [2 4]]
----------------------------------------
[[1 2]
 [3 4]]
[[-2.   1. ]
 [ 1.5 -0.5]]
----------------------------------------
[[1 2]
 [3 4]]
-2.0000000000000004
'''
```
## numpy 인덱싱
```python
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

'''
결과값
[10 20 30 40 50 60]
----------------------------------------
30
[20 40 60]
[50 60]
----------------------------------------1차원 끝
30  - arr2[0,2]
[[10 20 35]
 [40 50 60]
 [70 80 90]]  - arr2[0,2] 자리에 35값 넣음
[[10 20 55]
 [40 50 60]
 [70 80 90]]  - arr2[0][2] 자리에 55값 넣음
----------------------------------------인덱싱한 배열값
[55 50 60 70 80 90]
----------------------------------------2차원 끝
[[10 20 55]
 [45 55 66]
 [70 80 90]]
----------------------------------------
[[ 10  20  55]
 [ 45  55  66]
 [145 155 166]]
----------------------------------------
[[ 10  20  55]
 [ 45  55  66]
 [145 155 166]]
----------------------------------------
[ 10 155]
'''
```

## 2차원 배열 인덱싱, 슬라이싱
```python
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
'''
결과값
[10 20 30 40 50 60]
----------------------------------------
[20 30 40]
[20 30 40 50 60]
[10 20 30 40]
----------------------------------------
[10 20 35 45 55 60]
----------------------------------------
[10 20 37 37 37 60]
----------------------------------------
[[10 20 30]
 [40 50 60]
 [70 80 90]]
----------------------------------------
[[50 60]
 [80 90]]
----------------------------------------
[50 60]
----------------------------------------
[[10 20 30]
 [40 50 60]
 [70 80 90]]
----------------------------------------
[[10 25 35]
 [40 55 65]
 [70 80 90]]
'''
```

## matplotlib
```python
# 간단한 그래프 출력 
from matplotlib import pyplot as plt
import numpy as np

data1 = 10,14,19,20,25

# 리스트 내용을 그래프로 출력 
plt.plot(data1)
plt.show()

# numpy 배열 이용
arr = np.array(data1)
plt.plot(arr)
plt.show()

```

## 기술 통계
 - 자료를 그래프나 숫자 등으로 요약하는 통계적 해우이 및 관련 방법
 - 데이터를 요약하고 시각화해서 잘 설명하는 것에 중점을 두며,
   데이터에 대해서 쉽게 설명하기 위해서 시각화를 많이 활용한다.
 - 기술통계에서 기본적으로 사용하는 것
```bash
    => 도수분포표
    => 히스토그램
    => 박스플롯(상자그림)
```
 - 요약 통계량
   - 평균, 중앙값, 표준편차, 범위(최소~최대), 사분위수 등을 많이 사용한다.
   - 요약통계량은 박스플롯으로 시각화하여 확인한다.
 
 - 사분위수
   - 25% : 1사분위 수, 하위 25% 
   - 55% : 2사분위 수, 중앙값 50% 
   - 75% : 3사분위 수, 하위 75%, 상위 25% 
 
 - 도수분포표
   - 전체데이터의 분포를 쉽게 확인
   
## Pandas 
 1. Series - 1차원 배열
 2. DataFrame - 2차원 배열
 
### Series
 - 라벨을 가지는 1차원 데이터
 - Series 데이터에서는 세로축 라벨: index 입력한 시퀀스 데이터: values
 
### DataFrame
 - 2차원 데이터
 - 데이터 구성: index, columns, values 
  - index: DataFrame의 세로축 라벨 / 행 / row
  - columns: DataFrame의 가로축 라벨 / 열 / 변수
  - values: DataFrame의 데이터
  
### Data 전처리 
 - 데이터 가공
 - 데이터 핸들링
 - 데이터 클리닝
```bash
1. query - 컬럼 데이터중에 조건에 맞는 행 데이터 추출
2. filter - 특정 컬럼 여러개 추출 / filter(['컬럼명','컬럼명'])
3. drop - 행 또는 열을 삭제 / drop(행이름 or 리스트[,option])
  - drop option -
    inplace : 삭제 결과를 원본에 반영할지 결정 / False:True
    axis
      - axis = 0 : x축 / 행에 대한 적용 / 기본값
      - axis = 1 : y축 / 열에 대한 적용
```
 - enumerate: data를 dict형식으로 가져옴
 
### 결측값 대치
 - 평균값, 중앙값, 최빈값으로 대치
 - use SimpleImputer