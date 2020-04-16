def exam11():
    tup1 = (1,2,3,4,5)
    list1 = [10,20,30,40,50]
    
    print("{} {} {} {}".format(*tup1))
    print("{} {} {} {}".format(*list1))
    
    print("{1} {2} {3} {4}".format(*tup1))
    print("{4} {3} {2} {1}".format(*list1))
    
    # 일반 변수에 튜플 저장하기
    # unpacking : 튜플의 데이터 개수와 변수의 개수가 동일해야한다.
    a,b,c,d,e=tup1
    print(a,b,c,d,e)
    
    
exam11()
