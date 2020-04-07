def practice1():
    num1 = int(input('1~100 사이의 배수를 구할 숫자 입력 : '))
    count = 0
    for x in range(1,101):
        if x%num1==0:
            print(x, end=" ")
            count += 1
            
    print()
    print('1~100 사이의 %d의 배수 개수 = %d' %(num1, count))
    
practice1()