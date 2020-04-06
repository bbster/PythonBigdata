def exam4():
    # 위치값 0123456789 양수로 위치값 표시
    #        987654321 음수로 위치값 표시
    st1 = 'abcdefg'
    
    # 인덱싱 : [R] 특정위치의 문자 읽기
    
    print("st1 =", st1)
    print('st1[0]: ', st1[0])
    print('st1[3]: ', st1[3])
    print('st1[6]: ', st1[6])
    print('st1[-1]: ', st1[-1])
    print('st1[-4]: ', st1[-4])
    print('st1[-6]: ', st1[-6])
    print('-'*30)
    
    # 슬라이싱 [s:t] - s~t 문자열 추출
    print("st1 =", st1)
    print('st1[1:4]: ', st1[1:4])
    print('st1[:4]: ', st1[:4])
    print('st1[1:]: ', st1[1:])
    print('st1[-4:-1]: ', st1[-4:-1])
    print('st1[:-1]: ', st1[:-1])
    print('st1[-4:]: ', st1[-4:])
    print('-'*30)
    
    # 문자열 길이
    print(len(st1))
    print('st1: ', st1)
    st2 = 'x' + st1[2:]
    print('st2: ' + st2)
    
exam4()
