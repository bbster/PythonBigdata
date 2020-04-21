from pandas import DataFrame as df

# 딕셔너리를 원소로 갖는 리스트
grade_dic = [{'국어': 98,'영어': None,'수학': 88,'과학': 63},
             {'국어': 88, '영어': 90, '수학': 62,'과학': 50},
             {'국어': 92, '영어': 70, '수학': None,'과학': 70},
             {'국어': 63, '영어': 60, '수학': 31,'과학': None},
             {'국어': 23, '영어': 48, '수학': None,'과학': 69}]

# 딕셔너리의 키값이 컬럼의 이름으로 지정됨
# 리스트를 원소로 갖는 딕셔너리를 사용하면, 인덱스만 따로 지정함
data = df(grade_dic, index=['철수','영희','민철','수현','호영'])
print(data)
print('-'*40)

# 1. 컬럼(열)의 순서 변경
df1 = data.reindex(columns=['국어','수학','과학','영어'])
print(df1)
print('-'*40)
print(data)
print('-'*40)

# 2. 인덱스의 순서 변경
df2 = data.reindex(index=['호영','수현','민철','영희','철수'])
print(df2)
print('-'*40)
print(data)
print('-'*40)

# 3. 통째로 순서 변경
df3 = data.reindex(columns=['영어','수학','과학','국어'],
                   index=['호영','도희','철수','민아','민철'])
print(df3)
print('-'*40)
print(data)
print('-'*40)
