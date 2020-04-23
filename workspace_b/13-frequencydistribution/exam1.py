from pandas import DataFrame as df

grade_dic = [{'국어': 98,'영어': None,'수학': 88,'과학': 63},
             {'국어': 88, '영어': 90, '수학': 62,'과학': 50},
             {'국어': 92, '영어': 70, '수학': None,'과학': 70},
             {'국어': 63, '영어': 60, '수학': 31,'과학': None},
             {'국어': 23, '영어': 48, '수학': None,'과학': 69}]

data = df(grade_dic, index=['철수','영희','민철','수현','호영'])
print(data)
print('-'*40)

data_na = data.isna()
print(data_na)
print('-'*40)

# 각 열별로 결측치 수 파악하기
# 데이터프레임의 열별로 합게를 수행하면, True는 1, False는 0으로 계산
data_na_sum = data_na.sum()
print(data_na_sum)
print('-'*40)

