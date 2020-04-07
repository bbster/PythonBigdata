def exam4():
    # 방법 1
    total = 0
    i = 1
    while i<=10 :
        total += i # total = total + i
        i += 1 # i = i + 1
    
    print('total = ', total)
    
    # 방법 2
    total = 0
    i = 1
    while True :
        if i>10 : break
        total += i # total = total + i
        i += 1 # i = i + 1
    print('total = ', total)
    
exam4()