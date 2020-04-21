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


k1 = data.drop('국어', axis=1)
print(k1)
print('-'*40)

k2 = data.drop(['영어','수학','과학'], axis=1)
print(k2)
print('-'*40)

k3 = data.drop(data.columns[3], axis=1)
print(k3)
print('-'*40)
print(data)
print('-'*40)

k4 = data.drop(data.columns[1:4], axis=1)
print(k4)
print('-'*40)
print(data)
print('-'*40)

data.drop(data.columns[1:4], axis=1, inplace=True)
print(data)
print('-'*40)
