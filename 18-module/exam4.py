from datetime import date

print(date.today())
print('-'*30)

print(date(2019, 10, 5))
d = date(2019, 10, 5)
print(d)
print('{}/{}/{}'.format(d.year, d.month, d.day))
print('-'*30)

day1 = date(2019, 12, 31)
day2 = date.today()
day3 = date(2020, 12, 31)
day_num = day3 - day1
print('일수 : ',day_num)
