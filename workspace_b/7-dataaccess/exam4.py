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

# 1.하나의 행에 모든 데이터 추
# => 리턴값은 Series
cs = data.loc['철수']
print(cs)
print(type(cs))
print('-'*40)

# 2. 행의 값들을 읽기
# => 데이터 자료형은 numpy 배열
arr = data.loc['철수'].values
print(arr)
print(type(arr))
print('-'*40)

# 3. 행의 값들을 list로 변환
ls = list(data.loc['철수'])
print(ls)
print(type(ls))
print('-'*40)

# 4. 행슬라이싱 1: 행시작위치 / 행 < 행끝위치
data1 = data[0:2]
print(data)
print()
print(data1)
print('-'*40)

# 5. 행슬라이싱 2: 시작인덱스명 / 행 <= 종료인덱스
data2 = data.loc['영희':'수현']
print(data)
print()
print(data2)
print('-'*40)
