def exam1():
    x = int(input('정수입력 : '))
    y = int(input('정수입력 : '))
    doubleNum(x,y)
    
    
def doubleNum(x,y):
    if x%y==0 :
        print('%s는 %s의 배수입니다.' %(x,y))
        
    else :
        print('%s는 %s의 배수가 아닙니다.' %(x,y))
        
        
exam1()

