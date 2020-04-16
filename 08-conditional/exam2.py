def exam2():
    num1 = int(input("첫번째 정수 입력"))
    num2 = int(input("두번째 정수 입력"))
    
    if num2 > num1 :
        num1, num2 = num2, num1
        print("큰값: %d, 작은값: %d"  %(num1,num2))

exam2()