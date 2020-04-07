def exam2():
    list1 = []
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.append([4,5])
    list1.append([4,[4,5]])
    list1.pop()
    
    print(list1)
    print('항목 갯수: ', len(list1))
    print(list1[0], list1[4])
    
exam2()