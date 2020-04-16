def exam2():
    num1 = 5
    num2 = 7.7
    num3 = True
    num4 = "Hello World"

    # - 결합 -
    # 정수 + 실수 = 실수
    # 문자열 + 숫자 = 에러
    # 문자열 + str(숫자) = 문자열숫자
    
    print(num1 + num2)
    print('합 : ' + str(num1+num2))
    print('진실 : ' + str(num3))
    
    #문자열을 숫자로 바꾸기 / 문자열이 숫자여야만함
    str1 = '123123123'
    str2 = '3.14'
    s1 = int(str1)
    s2 = float(str2)
    print(s1, type(s1))
    print(s2, type(s2))
    
exam2()
