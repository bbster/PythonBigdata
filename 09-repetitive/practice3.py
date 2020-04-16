def practice3():
    while True:
        num1 = int(input('몇 단을 출력지 입력하시오: '))
        for y in range(1, 10):
            result = num1 * y
            print('%s * %s = %s' %(num1,y,result))         
        select = input('선택하시오(y:계속): ')
        print()
        if select == 'y' :
            continue
        else:
            break

practice3()
