from pandas import DataFrame as df

# 딕셔너리를 원소로 갖는 리스트
grade_dic = [{'국어': 98, '영어': None, '수학': 88,'과학': 63},
             {'국어': 88, '영어': 90, '수학': 62,'과학': 50},
             {'국어': 92, '영어': 70, '수학': None,'과학': 70},
             {'국어': 63, '영어': 60, '수학': 31,'과학': None},
             {'국어': 23, '영어': 48, '수학': None,'과학': 69}]

# 딕셔너리의 키값이 컬럼의 이름으로 지정됨
# 리스트를 원소로 갖는 딕셔너리를 사용하면, 인덱스만 따로 지정함
data = df(grade_dic, index=['철수','영희','민철','수현','호영'])
print(data)
print('-'*40)

# 1. 단일 조건
# => 기본적인 비교식을 사용한다
# 국어점수 > 80 인 학생 조회
result = data.query('국어 > 80')
print(result)
print('-'*40)

# 2. and 조건 사용
# 국어점수가 80점을 넘고, 수학점수도 80점 넘는 학생
result = data.query('국어 > 80 and 수학> 80')
print(result)
print('-'*40)

# 3. or 조건 사용
# 국어 점수가 70점 미만이거나 수학점수가 70점 미만인 학생 조회
result = data.query('국어 < 70 or 수학 < 70')
print(result)
print('-'*40)

# 4. in 조건 사용
# 특정 리스트의 원소중 겹치는 값 찾기

# 검색 조건에 대한 리스트 준비
item = [98,88]
print('리스트 값 : ', item)

# item 리스트에 포함되어 있는 국어점수 데이터 찾기
result2 = data.query('국어 in @item')
print(result2)
print('-'*40)

# 5. not in 조건 사용 
# 특정 리스트의 원소와 겹치지 않는 값 찾기
# item 리스트에 포함되지 않는 국어점수 데이터 찾기
print('리스트 값 : ', item)
result2 = data.query('국어 not in @item')
print(result2)
print('-'*40)
