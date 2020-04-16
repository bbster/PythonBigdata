def exam7():
    name = ['홍길동', '김철수', '민도희']
    score = [[] for j in range(3)] # 
    
    #print(score)
    score[0].append(75)
    score[0].append(52)
    score[0].append(95)
    
    score[1].append(72)
    score[1].append(52)
    score[1].append(48)
    
    score[2].append(16)
    score[2].append(45)
    score[2].append(77)
    
    tot = [0,0,0]
    for a in range(len(tot)):
        tot[a] = sum(score[a])
        
    for x in range(len(score)):
        print('{}, 총점={}, 평균={}'.format(name[x], tot[x], tot[x]/3))
    
exam7()
