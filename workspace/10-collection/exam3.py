def exam3():
    str_list = ['국어', '영어', '수학', '사회']
    print(str_list)
    
    # slicing
    list1 = str_list[1:3]
    print('list1 :', list1, type(list1))
    list1 = str_list[:3]
    print('list1 :', list1)
    list1 = str_list[1:]
    print('list1 :', list1)
    print('-'*60)
    
    # 데이터 검사
    if '사회' in str_list:
        print(str_list.index('사회'))
        
        print('-'*60)
    
exam3()
    