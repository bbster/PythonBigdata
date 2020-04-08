dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dict1)
print('='*60)

# key값 유무 확인
print('c' in dict1)
print('Hello' in dict1)
print('='*60)

# data값 유무 확인은 안됨.

# 개별 데이터 확인
# 1. indexing 방법
# 2. get() 함수 사용
print(dict1['a'])
print(dict1.get('c'))
print('='*60)

print(dict1.get('f')) # 없는 키값 사용시 None 출력
print('='*60)

# for
for key in dict1.keys():
    print(key, end=', ')

print()
print('='*60)

for value in dict1.values():
    print(value, end=', ')

print()
print('='*60)

for key, value in dict1.items():
    print(key, value, end=', ')
    
print()
print('='*60)

# 정렬
for key in sorted(dict1.keys(), reverse=True):
    print(key, dict1[key], end=', ')
    
print()
print('='*60)
# 데이터 갯수 확인
print(len(dict1), '개')
print('='*60)
# 데이터 추가
# 데이터 1개 추가
dict1['e'] = '빅데이터'
print(dict1)
print('='*60)

dict1.update({'f':'Java', 'g':'Spring'})
print(dict1)
print('='*60)
