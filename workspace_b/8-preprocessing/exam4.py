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

# 1. 특정행 삭제하기
# => inplace 속성을 설정하지 않으면, 원본은 그대로 있
d1 = data.drop('철수')
print(d1) # 철수를 보내버렸다.
print(data) # 철수가 다시 돌아왔다.
print('-'*40)

# 2. 여러 행 삭제하기
d2 = data.drop(['철수','영희','민철']) # filter와 다르게 []를 생략 할수가 있다.
print(d2) # 철수 영희 민철이를 보냈다.
print(data) # 다시 돌아왔다. 
print('-'*40)

# 3. 인덱스 번호로 삭제하기
d3 = data.drop(data.index[0]) # 0번째 행 삭
print(d3) # 철수를 보냈다.
print(data) # 다시 돌아왔다. 
print('-'*40)

# 4. 슬라이싱을 통한 범위 내의 행 삭제하기
d4 = data.drop(data.index[1:4])
print(d4) # 철수 영희 민철이를 보냈다.
print(data) # 다시 돌아왔다. 
print('-'*40)

# 5. 삭제결과를 원본에 반영하기
# => Use inplace option
data.drop(data.index[1:4], inplace=True)
print(data) # 철수 영희 민철이를 영원히 보냈다.
print('-'*40)
