def exam4():
    list1 = [1,2,3]
    print(list1)
    
    # 인덱싱으로 변경
    list1[2] = 40
    print(list1)
    list1[1] = ['a', 'b', 'c']
    print(list1)
    
    # 슬라이싱으로 변경
    list1[1:2] = ['a', 'b', 'c']
    print(list1)
    list1.append('d')
    print(list1)
    
    list1[1:3] = 10,20
    print(list1)
    
    
exam4()
    