def exam8():
    a = (1,2,3)
    b = (4,5,6)
    c= a+b
    d=a*3
    print(c)
    print(d)
    
    tup1 = (10,20,30,40,50,30)
    tup2 = ('c언어', 'Python', 'Java', 'JSP')
    
    print(len(tup1))
    print(max(tup1))
    print(min(tup1))
    print(sum(tup1))
    print(sorted(tup1))
    print(sorted(tup1, reverse=True))
    
    print('='*60)
    
    tup5 = (0 for a in range(5))
    print(tup5)
    
    
exam8()