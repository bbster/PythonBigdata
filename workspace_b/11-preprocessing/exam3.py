from pandas import DataFrame as df
import numpy as np

city_people = {
    '도시' :['서울', '서울','서울','부산','부산','부산','인천','인천'],
    '연도' : ['2010','2015','2013','2015','2010','2015','2012','2011'],
    '인구' : [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890542, 2654123],
    '지역' : ['수도권','수도권','수도권','경상권','경상권','경상권','수도권','수도권',]
    }

census = df(city_people)
print(census)
print('-'*40)

# 2. 하나의 컬럼에 대해 여러개의 집계함수 동시 사용
# agg() 함수에 집계함수의 이름을 문자열 원소로 갖는 리스트로 설정
# => min max sum mean std var
city_people = census.filter(['도시','인구'])
print(city_people)
print('-'*40)

result2 = city_people.groupby(city_people['도시']).agg(['min','max','std','sum'])
print(result2)
print('-'*40)

# 행과 열의 구조 확인 
print(result2.columns)
print(result2.index)
print('-'*40)

# 3. 사용자 정의 함수를 적용하기
# x = 특정 컬럼에 대한 Series 객체
# 

def my_range(x):
    return np.max(x) - np.min(x)

result3 = city_people.groupby(city_people['도시'])\
            .agg(['min','max','std','sum',my_range])    
print(result3)
print('-'*40)

# 4. 여러 컬럼에 대해 서로 다른 집계함수 적용하기
# => 딕셔너리 형식으로 {컬럼명: [함수리스트], 컬럼명: [함수리스트]}
local_city_people = census.filter(['지역','도시','인구'])
print(local_city_people)
print('-'*40)

result4 = local_city_people.groupby(local_city_people['지역'])\
            .agg({'도시':['count'], '인구':['sum']})
print(result4)
print('-'*40)

# 행과 열의 구조 확
print(result4.columns)
print(result4.index)
print('-'*40)
