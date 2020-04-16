a = {1, 2, 3}
b = {1, 2, 3, 3}

print(a, len(a))
print(b, len(b))
print('='*60)

# 데이터 추가
a.add(5)
print(a, len(a))
print('='*60)

# 개별 데이터 확인
# 인덱싱으로 확인불가
# print(a[0])

# 1. for문 사용
for v in a:
    print(v, end=', ')
print()
print('='*60)
# 2. .pop() 사용 / 확인한 데이터가 삭제됨.
print(a, len(a))
print(a.pop())
print(a, len(a))
print('='*60)

# 데이터 유무 확인
print(2 in a)
print(2 not in a)
print('='*60)