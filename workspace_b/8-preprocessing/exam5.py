from pandas import DataFrame as df
from pandas import Series

# 딕셔너리를 원소로 갖는 리스트
grade_dic = [{'국어': 98,'영어': None,'수학': 88,'과학': 63},
             {'국어': 88, '영어': 90, '수학': 62,'과학': 50},
             {'국어': 92, '영어': 70, '수학': None,'과학': 70},
             {'국어': 63, '영어': 60, '수학': 31,'과학': None},
             {'국어': 23, '영어': 48, '수학': None,'과학': 69}]

# 딕셔너리의 키값이 컬럼의 이름으로 지정됨
# 리스트를 원소로 갖는 딕셔너리를 사용하면, 인덱스만 따로 지정함
data = df(grade_dic, index=['철수','영희','민철','수현','호영'])


# 1. 리스트를 활용한 열 추가
data['한국사'] = 92,83,72,None,80
print(data)
print('-'*40)

# 2. 단일값 추가
data['세계사'] = 100
print(data)
print('-'*40)

# 3. Series로 열 추가하기
# => 데이터의 갯수가 일치하지 않으면 빈곳에는 Nan이 자동입력됨
data['사회'] = Series([82,90,92,64], index=['철수','영희','민철','수현'])
print(data)
print('-'*40)

data['사회'] = Series([82,90,92,64])
print(data)
print('-'*40)

conditions = [
              (data['영어']>90),
              (data['영어']>=80),
              (data['영어']>=70),
              (data['영어']<70),
              (numpy.isnan(data['영어'])==True)
    ]
print(conditions)
print('-'*40)

grade = ['A', 'B', 'C', 'F', 'F']
data['영어학점'] = numpy.select(conditions, grade)
print(data)
print('-'*40)

