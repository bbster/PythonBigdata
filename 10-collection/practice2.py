days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
total_day = []

print('*** 일수 구하기 ***')
year = int(input('년도 : '))
month = int(input('월 : '))
day = int(input('일 : '))

# 윤년 확인
if (year%4==0) and (year%100 != 0) or (year%400==0):
    days[2] = 29
    print("윤년입니다")
    

for x in range(month):
    total_day.append(days[x])

total = sum(total_day) + day
print('%s년1월1일부터 %s월%s일까지는 %d일 입니다.' %(year,month,day,total))

'''
total = sum(days[1:month]) + day


for x in range(1, month):
    total_day += days[x]
    
total_day += day

    
'''