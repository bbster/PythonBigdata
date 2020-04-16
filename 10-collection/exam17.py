a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}
print('='*60)

# 교집합
c = a.intersection(b)
print(c)
print('='*60)

# 합집합
d = a.union(b)
print(d)
print('='*60)

# 차집합
e = a.difference(b)
print(e)
print('='*60)