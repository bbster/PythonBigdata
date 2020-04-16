def exam6():
    # 논리 연산자
    '''
    진리표
    x        y     x and y     x or y      not x
    True   True    True        True        False
    True   False   False       False       False
    False  True    False       True        True
    False  False   False       False       True
    '''
    
    r1 = 100 >= 200 # False
    r2 = 5 >= 3 # True
    
    print(r1 and r2) # False and True = False
    print(r1 or r2) # False or True = True
    print(not(r1 or r2)) # not (False or True) = False
    
    
exam6()