from pandas import DataFrame as df
from pandas import merge

# 데이터 생성
score_khistory = df({'한국사':[87,91]}, index=['영희','철수'])
print(score_khistory)
print('-'*40)

score_whistory = df({'세계사':[80,56], '이름':['영희','철수']})
print(score_whistory)
print('-'*40)

# 1. 왼쪽에서는 인덱스 사용, 오른쪽으로는 '이름'컬럼 사용
# => 인덱스가 사라지고, 모두 컬럼으로 지정되어짐

data = merge(score_khistory, score_whistory, left_index=True, right_on=['이름'])
print(data.head())
print('-'*40)

# 2. 이름 컬럼을 인덱스로 지정하고 삭제하기
name_list = list(data['이름'])
name_dict = {}

for i,v in enumerate(name_list):  # enumerate: data를 dict형식으로 가져옴
    name_dict[i] = v
    
data.rename(index=name_dict, inplace=True)
print(data.head(5))
print('-'*40)

data.drop('이름', axis=1, inplace=True)
print(data.head(5))
print('-'*40)
