dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dict1)
print('='*60)

print('{} {} {} {}'.format(*dict1))
print('='*60)

print('{a} {b} {c} {d}'.format(**dict1))