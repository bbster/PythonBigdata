def practice2():
    score1 = int(input('국어 점수 입력 : '))
    score2 = int(input('영어 점수 입력 : '))
    total = score1+score2
    avarage = total/2

    print('총점 = %d' %total)
    print('평균 = %f' %avarage)
    
    if avarage >=90 and avarage <=100 :
        print('A학점')
    elif avarage >=80 and avarage <=89 :
        print('B학점')
    elif avrage >=70 and avarage <=79 :
        print('C학점')
    elif avrage >=60 and avarage <=69 :
        print('D학점')
    elif avrage >=0 and avarage <=59 :
        print('F학점')

    

practice2()