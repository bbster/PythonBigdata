from pandas import date_range as dr

# 데이터 생성
s1 = dr(start='2020-01-01', end='2020-01-04') # 기본 1일씩 증가
print(s1)
print(type(s1))
print('-'*40)

s1 = dr(start='2020/1/1', periods=4)
print(s1)
print(type(s1))
print('-'*40)

s1 = dr(start='2020/1/1', periods=4, freq='2D')
print(s1)
print(type(s1))
print('-'*40)

# freq ='W' : 일요일을 시작기준으로 일주일 주기
s1 = dr(start='2020/1/1', periods=4, freq='W')
print(s1)
print(type(s1))
print('-'*40)

# BM : 업무 월말 날짜 기준 주기
# 2BM : 업무일 기준 2개월 월말 주
s1 = dr(start='2020/1/1', periods=4, freq='BM')
print(s1)
print(type(s1))
print('-'*40)

s1 = dr(start='2020/1/1', periods=4, freq='2BM')
print(s1)
print(type(s1))
print('-'*40)

li = list(s1)
print(li)
print(type(li))
