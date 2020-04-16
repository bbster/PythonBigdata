# 추가모드로 쓰기

f = open('test.txt', 'a')
for i in range(11, 16):
    data = str(i) + '번째 줄입니다. \n'
    f.write(data)
    
f.close()

f = open('test.txt', 'r')
u = f.readlines()
print(u)
f.close()
