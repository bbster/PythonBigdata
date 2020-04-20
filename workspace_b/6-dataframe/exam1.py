from pandas import DataFrame as df

# 어느 학급의 성적표를 표현한 2차원 리스트
#            국   영  수 사 과
grade_list = [[98, None, 88, 64], # 철수씨
              [88,90,62,72],  # 영희씨
              [92,70,None,None], 
              [63,60,31,70],
              [120,50,None,88]
              ]

# 행과 열을 갖는 표 형태의 DataFrame 생성 
data = df(grade_list)
print(data)
print(type(data))
print('-'*40)

# 컬럼이름 지정
# 컬럼이름은 리스트로 지정 
c_names = '국어','영어','수학','과학'
data = df(grade_list, columns=c_names)
print(data)
print(type(data))
print('-'*40)

# 인덱스 이름 지정
i_names = '철수','영희','민철','수현','호영'
data = df(grade_list, columns=c_names, index=i_names)
print(data)
print(type(data))
print('-'*40)
