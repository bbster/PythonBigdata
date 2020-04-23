from pandas import DataFrame as df
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer 

grade_dic = {'국어': [98,88,92,63],
             '영어': [90,70,60,None],
             '수학': [63,50,None,69],
             '과학': [None,70,31,48]}
             
data = df(grade_dic, index= ['철수','영희','민철','수현'])
print(data)
print(type(data))
print('-'*40)

# 결측지가 포함된 모든 행 삭제
# 행에 포함된 값 중 하나라도 결측치가 있는 경우 삭제
na1 = data.dropna()
print(na1)
print('-'*40)

# 행에 포함된 모든 값이 결측치인 경우만 삭제
# 삭제될 가능성이 매우 적다.
na2 = data.dropna(how='all')
print(na2)
print('-'*40)

# 결측치가 포함된 모든 열 삭제
na3 = data.dropna(axis=1)
print(na3)
print('-'*40)

na4 = data.dropna(axis=1, how='all')
print(na4)
print('-'*40)
