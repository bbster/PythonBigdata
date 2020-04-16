def exam6():
    hong = []
    hong.append(75)
    hong.append(82)
    hong.append(95)
    
    kim = []
    kim.append(88)
    kim.append(64)
    kim.append(70)
    
    lee = [100,95,90]
    
    tot = [0,0,0]
    for x in hong :
        tot[0] += x
        
    for x in kim :
        tot[1] += x
        
    for x in lee :
        tot[2] += x
        
    print('홍길동 : ', tot[0] / len(hong))
    print('김용국 : ', tot[1] / len(kim))
    print('이지찬 : ', tot[2] / len(lee))
exam6()