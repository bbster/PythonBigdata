students = []

with open('test.csv', 'r') as f:
    lines = f.readlines()
    
    for line in lines:    
        line = line.replace('\n','')
        print(line.split(','))
        
        students.append(line.split(','))
        
        
print('students : ')
print(students)

for student in students :
    name, kor, eng, mat = student
    tot = int(kor) + int(eng) + int(mat)
    avg = tot/3
    result = '''이름: {}, 국어: {}, 영어:{}, 수학:{} 총점: {}, 평균: {:.1f}'''.format(name,kor,eng,mat,tot,avg)
    
    print(result)
        