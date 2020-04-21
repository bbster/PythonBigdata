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

# 1. 컬럼이름 변경하기
df1 = data.rename(columns={'국어':'kor','영어':'eng',
                           '수학':'math','과학':'sinc'})
print(df1)
print(data)
print('-'*40)

# 2. 인덱스 이름 변경하기
df2 = data.rename(index={'영희':'yh','철수':'cs','민철':'mc',
                         '수현':'sh','호영':'hy'})
print(df2)
print(data)
print('-'*40)

# 3. 컬럼 인덱스 동시 변경

df3 = data.rename(columns={'국어':'kor','영어':'eng',
                           '수학':'math','과학':'sinc'},
                  index={'영희':'yh','철수':'cs','민철':'mc',
                         '수현':'sh','호영':'hy'},
                  inplace=True)
print(df3)
print('-'*40)
