'''
SIZE = 5
score = []
rank = []

for x in range(SIZE) :
    temp = int(input(str(x+1) + '번 점수 입력 : '))
    score.append(temp)
    rank.append(1)
    
#  선택 정렬 
for x in range(len(score)): # 기준값
    for y in range(len(score)): # 비교값
        if(score[x] < score[y]) : rank[x] += 1

print('***결과***')
for x in range(len(score)):
    print('{}점 : {}등'.format(score[x], rank[x]))
'''
SIZE = 5
score = {}

for x in range(SIZE) :
    temp = int(input(str(x+1) + '번 점수 입력 : '))
    score[temp] = 1
    
for x in score.keys(): # 기준값
    for y in score.keys(): # 비교값
        if(x < y) : score[x] += 1
        
print('***결과***')
for x in score.keys():
    print('{}점 : {}등'.format(x, score[x]))
