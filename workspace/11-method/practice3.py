def add(x=1, y=100):
    # 디폴트 1~100 사이의 합
    # 인수 한개전달 x~100
    # 인수 두개 전달 x~y
    g=0
    for z in range(x,y+1):
        g += z
    
    return g


print(' 1 ~ 100 사이의 합 : ', add())
print(' 30 ~ 100 사이의 합 : ', add(30))
print(' 20 ~ 200 사이의 합 : ', add(20, 200))