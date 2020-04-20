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

# 1. 인데스 이름 확인
print(data.index)
print(type(data.index))
print('-'*40)

i_list = list(data.index)
print(i_list)
print(type(i_list))
print('-'*40)

# 2. 컬럼이름 확인
print(data.columns)
print(type(data.columns))
print('-'*40)

c_list = list(data.columns)
print(c_list)
print(type(c_list))
print('-'*40)


# 3. 데이터 확인
print(data.values)
print(type(data.values))
print('-'*40)

# 4. 전치 구하기
df_t = data.T
print(df_t)
print(type(df_t))
print('-'*40)
