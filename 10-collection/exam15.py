dic = {101:'사과', 102:'복숭아', 103:'감', 104:'바나나'}
print(dic)
print('='*60)

# 리스트 형탤 ㅗ변환해서 사용
list_keys = list(dic.keys())
print(dic.keys(), type(dic.keys()))
print(list_keys)
print(type(list_keys))
print('='*60)

list_values = list(dic.values())
print(dic.values(), type(dic.values()))
print(list_values, type(list_values))
print('='*60)

list_items = list(dic.items())
print(list_items, type(list_items))
print('='*60)
