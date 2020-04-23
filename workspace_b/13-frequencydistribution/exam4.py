from pandas import DataFrame as df
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer as simp
import numpy as np


grade_dic = {'국어': [98,88,92,63],
             '영어': [90,70,60,None],
             '수학': [63,50,None,69],
             '과학': [None,70,31,48]}
             
data = df(grade_dic, index= ['철수','영희','민철','수현'])

simple_imp = simp(missing_values=np.nan, strategy='mean')
print(simple_imp)
print('-'*40)

result_simple_imp = simple_imp.fit_transform(data.values)
print(result_simple_imp)
print('-'*40)

data_result = df(result_simple_imp, index=data.index, columns=data.columns)
print(data_result)
print('-'*40)

# 이상치 존재여부 확인을 위해 상자그림 표시

# 그래프 기본 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 16
plt.rcParams['figure.figsize'] = (10,6)

# 상자그림 출력
data_result.boxplot()
plt.show()

# 이상치를 결측치로 변경하기
# 국어점수에 대한 이상치 필터링
data_outlier = data_result.query('국어 > 80')
print(data_outlier)
print('-'*40)

# 필터링 된 이상치 데이터에 대한 인덱스 추출
outlier_index = list(data_outlier.index)
print(outlier_index)
print('-'*40)

# 이상치를 갖는 인덱스에 대한 국어점수를 결측치로 변경
for i in outlier_index:
    data_result.loc[i,'국어'] = np.nan

print(data_result)
print('-'*40)

# 변경된 결치 정제
# 결측치에 대해 평균점수 부여 
# 63점 하나밖에 없어서 Nan 값이 모두 63점으로 들어
result_simple_imp1 = simple_imp.fit_transform(data_result.values)
print(result_simple_imp1)
print('-'*40)

# 정제된 결과로 데이터프레임 생
df1_result = df(result_simple_imp1, index=data_result.index,
                                    columns=data_result.columns)

print(data)
print(df1_result)
print('-'*40)
