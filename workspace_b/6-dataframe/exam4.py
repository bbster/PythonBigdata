from pandas import DataFrame as df
from pandas import read_csv  # csv파일을 읽어들이기 위한 함

# 외부에서 csv나 xlsx 파일을 가져오는 경우
# index가 인식되지 않기 때문에 특정 컬럼의 값들을 index로 지정
# 그 컬럼을 삭제하는 전처리가 필요 
# 기본 encoding 값 UTF-8
data = read_csv('../data/grade.csv', encoding='euc-kr')
print(data)
print(type(data))

data = read_csv('../data/grade1.csv')
print(data)
print(type(data))
