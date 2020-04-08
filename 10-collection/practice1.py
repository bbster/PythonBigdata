score = []
SIZE = 5
for x in range(SIZE):
    temp = int(input(str(x+1) + '번의 학생의 점수를 입력 : '))
    score.append(temp)
    
total = sum(score)
avg = total/ len(score)
print('총점 : %s, 평균 : %s' %(total,avg))

    