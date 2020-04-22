from pandas import DataFrame as df
import numpy as np

city_people = {
    '도시' : ['서울', '서울','서울','부산','부산','부산','인천','인천'],
    '연도' : ['2011','2012','2013','2014','2015','2016','2017','2018'],
    '인구' : [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890542, 2654123],
    '지역' : ['수도권','수도권','수도권','경상권','경상권','경상권','수도권','수도권',]
    }

census = df(city_people)
print(census)
print('-'*40)

# 2. 피벗테이블 : 각 도시별 연도에 따른 인구수
# pivot(index, columns, values)
pv1 = census.pivot(index='도시', columns='연도', values='인구')
print(pv1)
print('-'*40)

print(pv1.columns)
print(pv1.index)
print('-'*40)

# 3. 피벗 테이블 생성 제약
# => 컬럼과 인덱스이름으로 사용되는 데이터의 쌍이 중복되는 경우가 있으면 안된다

# 지역과 연도에 대한 조합은 두쌍이 나타나므로 에러
pv2 = census.pivot('지역', '연도', '인구')
print(pv2)

# 4. 그룹분석 결과를 피벗테이블로 조합하기
