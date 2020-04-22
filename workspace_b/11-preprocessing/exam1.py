from pandas import DataFrame as df

# 딕셔너리를 원소로 갖는 리스트
grade_dic = {'국어': [98,88,92,63],
             '영어': [90,70,60,48],
             '수학': [63,50,70,69],
             '과학': [62,70,31,48]}
             

# 딕셔너리의 키값이 컬럼의 이름으로 지정됨
# 리스트를 원소로 갖는 딕셔너리를 사용하면, 인덱스만 따로 지정함
data = df(grade_dic, index= ['철수','영희','민철','수현'])
print(data)
print(type(data))
print('-'*40)

# 2. 전체 열에 대한 집계
# 과목별 총점
print('data.sum() :')
print(data.sum())
print(type(data.sum()))
print('-'*40)

# 과목별 평균
print('data.mean() :')
print(data.mean())
print(type(data.mean()))
print('-'*40)

# 특정열에 대한 집계
print(data['국어'].sum())
print(data['국어'].mean())
print(data['국어'].max())
print(data['국어'].min())
print('-'*40)

# 4. 행 단위 집계
# 집계함수에 axis=1을 지정한다

# 학생별 총점
print(data.sum(axis=1))
print('-'*40)

print(data.mean(axis=1))
print('-'*40)

# 5. 특정 행에 대한 집계
# '영희'의 총점, 평균점수
print(data.loc['영희'].sum())
print(data.loc['영희'].mean())
print('-'*40)

# 6. 행단위 집계 결과를 새로운 열로 추가하기

# 학생별 총점과 평균 산출
tot = data.sum(axis=1)
print(tot)
print('-'*40)

avg = data.mean(axis=1)
print(avg)
print('-'*40)

# 산출한 집계결과를 새로운 열로 추가
data['총점'] = tot
data['평균'] = avg
print(data)
print('-'*40)

