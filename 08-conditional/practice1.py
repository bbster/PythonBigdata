def practice1():
    fnum1 = float(input('첫 번째 실수 입력: '))
    fnum2 = float(input('두 번째 실수 입력: '))
    operator = str(input('연산자를 입력:'))
    
    '''
    if operator == '+':
        print('%f %s %f = %f' %(fnum1, operator, fnum2, fnum1+fnum2))
    elif operator == '-':
        print('%f %s %f = %f' %(fnum1, operator, fnum2, fnum1-fnum2))
    elif operator == '*':
        print('%f %s %f = %f' %(fnum1, operator, fnum2, fnum1*fnum2))
    elif operator == '/':
        print('%f %s %f = %f' %(fnum1, operator, fnum2, fnum1/fnum2))
    else:
        print('연산자 입력이 잘못되었습니다.')
        '''
        
    if operator == '+' : result = fnum1 + fnum2
    elif operator == '-' : result = fnum1 + fnum2
    elif operator == '*' : result = fnum1 + fnum2
    elif operator == '/' : result = fnum1 + fnum2
    
    print('%s %s %s = %s' %(fnum1, operator, fnum2, result))
practice1()
