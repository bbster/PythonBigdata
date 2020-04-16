def exam1():
    print(range(5))
    print(range(1, 11, 2))
    print(type(range(5)))
    
    a =''
    for x in range(10):
        a += str(x) + ' '
        
    print(a)
    print('-'*30)
    
    for x in range(1, 11, 2) :
        print(x, end=" ")

exam1()