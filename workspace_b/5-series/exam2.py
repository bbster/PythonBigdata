from pandas import Series as sr

items = 10,30,50,70,90
column = sr(items)
print(column)
print(type(column))
print('-'*40)

# 시리즈의 색인(index)만 추출
i = column.index
print(i)
print(type(i))
print('-'*40)

# 시리즈의 색인을 리스트로 변환
index_list = list(i)
print(index_list)
print(type(index_list))
print('-'*40)

# 시리즈의 값들만 추출
v = column.values
print(v)
print(type(v))
print('-'*40)

# 시리즈의 값들을 리스트로 변
value_list = list(v)
print(value_list)
print(type(value_list))
print('-'*40)

# 특정 조건에 맞는 항목들만 추출
# 시리즈이름[이름에 대한 조건식]
# -> 30초과인 항목들만 추출
in1 = column[column > 30]
print(in1)
print(type(in1))
print('-'*40)

# and 조건
# -> 70이하 and 10초과인 항목들만 추
in1 = column[(column>10) & (column<= 70)]
print(in1)
print(type(in1))
print('-'*40)

# or 조건
# -> 10이하 or 70이상인 항목들만 추출
in3 = column[(column<=10) | (column>=70)]
print(in3)
print(type(in3))
print('-'*40)
