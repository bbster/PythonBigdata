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

# 1. 각 열별로 데이터 타입 확인
print(data.dtypes)
print('-'*40)

# 2. 특정 열에 대한 타입과 값 확인
print(data['국어'])
print('-'*40)
print(data['영어'].dtype)
print(type(data))
print('-'*40)

# 3. 특정 열의 값들을 읽기, 
arr = data['국어'].values
print(arr)
print(type(arr))
print('-'*40)

# 4. 열의 값들을 list 변환
k_list = list(data['국어'])
print(k_list)
print(type(k_list))
print('-'*40)

