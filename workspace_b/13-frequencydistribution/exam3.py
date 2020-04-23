from pandas import DataFrame as df
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer as simp
import numpy as np


grade_dic = {'국어': [98,88,92,63],
             '영어': [90,70,60,None],
             '수학': [63,50,None,69],
             '과학': [None,70,31,48]}
             
data = df(grade_dic, index= ['철수','영희','민철','수현'])

print('-'*40)

# None 값을 대표값으로 대체
data_fillna = data.fillna(value=50)
print(data_fillna)
print(type(data_fillna))
print('-'*40)

# 통계분석 기법으로 대체하기
# 결측치를 정제할 규칙 정의
# strategy option : mean=평, median=중앙값, most_frequent: 최빈값(가장많이 관측되는 값)
# simpleimputer 객체
# 각 열단위로 평균을 결측치에 지정

simple_imp = simp(missing_values=np.nan, strategy='mean') # 정제규칙 지정
print(simple_imp)
print(type(simple_imp))
print('-'*40)

result_simple_imp = simple_imp.fit_transform(data.values)
print(result_simple_imp)
print('-'*40)

print(data.mean())
print('-'*40)

# 적용된 규칙으로 새로운 데이터프레임 생성
data_result = df(result_simple_imp, index=data.index, columns=data.columns)
print(data_result)
print('-'*40)
