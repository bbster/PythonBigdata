def exam4():
    score = int(input("점수 입력 : "))
    
    if score >= 90:
        print('A학점')
    elif score >= 80:
        print('B학점')
    elif score >= 70:
        print('C학점')
    elif score >= 60:
        print('D학점')
    else:
        print('F학점')
    
    
exam4()