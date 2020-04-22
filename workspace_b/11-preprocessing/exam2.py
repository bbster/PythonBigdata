from pandas import DataFrame as df

city_people = {
    '도시' :['서울', '서울','서울','부산','부산','부산','인천','인천'],
    '연도' : ['2010','2015','2013','2015','2010','2015','2012','2011'],
    '인구' : [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890542, 2654123],
    '지역' : ['수도권','수도권','수도권','경상권','경상권','경상권','수도권','수도권',]
    }

census = df(city_people)
print(census)
print('-'*40)

# 2. 15년가느이 도시별 최대 인구수
# 하나의 컬럼을 집단별로 나누고 그룹분석 수행하기
# 분석을 할 컬럼만 추출
city_people = census.filter(['도시','인구'])
print(city_people)
print('-'*40)

# 특정 컬럼을 그룹으로 묶고 다른 컬럼으로 집계 수행
# => 그룹으로 묶인 컬럼은 인덱스로 구성된다.
# => 도시별 최대 인구수
city_people_max = city_people.groupby(city_people['도시']).max()
print(city_people_max)
print('-'*40)

# 열과 행의 구성확인
print(city_people_max.columns)
print(city_people_max.index)
print('-'*40)

