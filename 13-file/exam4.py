with open('test.txt', 'w') as f:
    for i in range(1, 6):
        data = str(i) + '번째 줄입니다. \n'
        f.write(data)
    
with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
