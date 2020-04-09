# 파일 읽기 1
f = open('test.txt', 'r')
text = f.read()
f.close()
print(text)



# 파일 읽기 2
f = open('test.txt', 'r')
while True:
    line = f.readline() # 한줄씩 찍기
    if not line : break
    print(line, end='')

f.close()
print()

# 파일 읽기 3
f = open('test.txt', 'r')
lines = f.readlines() # 모든 라인을 읽어서, 각각의 라인을 리스트로 줌
f.close()
print(lines)

for line in lines:
    print(line)
    
f.close()

# 파일 읽기 4
f = open('test.txt', 'r')
for line in f.readlines() :
    print(line, end='')
    
print()
f.close()