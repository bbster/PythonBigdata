def exam8():
    '''
    아이덴티티 연산자
    is : 레퍼런스 변수의 주소값이 같은지 검사
         => 연산 결과는 True 또는 False
         => True : 레퍼런스 값이 같음
            False : 레퍼런스 값이 다름
    is not: 레퍼런스 변수의 주소값이 같지 않은지 검사
         => 연산 결과는 True 또는 False
         => True : 레퍼런스 값이 다름
            False : 레퍼런스 값이 같음
            
    레퍼런스(reference) : 객체를 가르키는 주소값
    ref(x)를 통해 main함수 안에 있는 인자를 가르키고
    ref 함수에서는 매개변수 n을 통해 인자의 레퍼런스 값 즉 x를 받는다
    이를 값에 의한 전달(pass-by-value)라고 부른다
    ex)
    def main():
        x = 1
        ref(x)
    def ref(n):
        n += 1
        print(n) => 2
    '''
    a=1
    b=2
    c=3
    d=4
    print('a is b :', a is b)
    print('a is c :', a is c)
    print('a is d :', a is d)
    
    print('id(a): ', id(a))
    print('id(b): ', id(b))
    print('id(c): ', id(c))
    print('id(d): ', id(d))
    
    print('a is not b :', a is not b)
    print('a is not c :', a is not c)
    print('a is not d :', a is not d)
        
exam8()