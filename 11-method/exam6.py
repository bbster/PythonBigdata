def inputNum(n):
    for x in range(len(n)):
        n[x] = int(input(str(x+1) + '번째 숫자 입력 : '))


def outputNum(n):
    for x in range(len(n)):
        print(n[x], end=' ')
        

n = [0 for x in range(5)]
inputNum(n)
outputNum(n)
