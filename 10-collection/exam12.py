def exam12():
    dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
    print(dict1)
    print('='*60)
    
    # indexing 
    print(dict1['a'])
    print(dict1['b'])
    print(dict1['c'])
    print(dict1['d'])
    print('='*60)
    
    # key값만 읽어오기
    dic_key = dict1.keys()
    print(dic_key)
    
    # value값만 읽어오기
    dic_value = dict1.values()
    print(dic_value)
    
    # key, value 쌍으로 읽어오기
    dic_item = dict1.items()
    print(dic_item)
    
    # 데이터 추가
    dict1['phone'] = '010-1234-5678'
    print(dict1)
    
    # 데이터 1개 삭제
    del(dict1['b'])
    print(dict1)
    
    # 모든 데이터 삭제
    dict1.clear()
    print(dict1)
    
    # 기본적으로 {} 형태는 dict형태로 인식하지만
    # {} 안에 단순 데이터들은 세트로 인식하고
    # {key:value} key value 형태는 dict 형태로 인식한다.
    test1 = {}
    print(type(test1)) # dict
    
    test2 = {1}
    print(type(test2)) # set
    
    test3 = {'a':'b'}  
    print(type(test3)) # dict
    
    
exam12()