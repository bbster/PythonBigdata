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

# 1. 열단위 필터링 
# => 추출할 컬럼의 이름을 리스트로 전달한다.
result = data.filter(['국어', '영어'])
print(result)
print(type(result))
print('-'*40)

result = data.filter(['국어'])
print(result)
print(type(result))
print('-'*40)

result = data.filter('국어') # [] 생략할수 없
print(result)
print(type(result))
print('-'*40)

# 2. 열단위 조건 검색
# 영희가 70점을 넘기지 못한 과목 조회
# 전치로 변환한 후, 열을 필터링하고 query를 적용

# 1) 전치 구하기
d2 = data.T
print(d2)
print(type(d2))
print('-'*40)

# 2) 전치에서 원하는 열만 추출
r1 = d2.filter(['영희'])
r2 = d2['영희']
print(r1)
print(r2)
print('-'*40)

# 3) 추출된 결과에 대한 조건 검색
result = r1.query('영희 < 70')
print(result)
print('-'*40)

# query는 DataFrame에 있는 명령이므로, 
# Series에 데이터는 사용 못함.
#result = r2.query('영희 < 70')
#print(result)
#print('-'*40)

 