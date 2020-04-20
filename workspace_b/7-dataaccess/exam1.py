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

# 1. 데이터의 크기
# tuple type 속성 :  (행, 열)출력
print(data.shape)
print('row : ', data.shape[0])
print('cols : ', data.shape[1])
print('-'*40)

# 2. 상위 데이터 3건만 확인 / DataFrame . head
top3 = data.head(3)
print(top3)
print(type(top3))
print('-'*40)

# 3. 하위 데이터 3건만 확인 / DataFrame . tail
last3 = data.tail(3)
print(last3)
print(type(last3))
print('-'*40)

