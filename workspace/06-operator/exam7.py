def exam7():
    '''
    소속 연산자
    in : 어떤 데이터가 특정 데이터안에 존재하는지 검사
      결과값은 True 또는 False
      True : 존재함 False : 존재하지 않음
      
    not in : 어떤 데이터가 특정 데이터안에 존재하는지 않는지 검사
     결과값은 True 또는 False
     True : 존재하지 않음 False : 존재함
    '''
    st1 = 'abcdefg'
    print('st1 = ', st1)
    print('"ab" in st1 : ', "ab" in st1)
    print('"xy" in st1 : ', "xy" in st1)
    print('-'*30)
    print('st1 = ', st1)
    print('"ab" not in st1 : ', "ab" not in st1)
    print('"xy" not in st1 : ', "xy" not in st1)
exam7()