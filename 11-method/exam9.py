def calc_area(r):
    # 전역 변수를 사용하기 위해서는 전역변수 선언을 먼저 해야 함
    global area
    area = 3.14 * r**2
    

area = 0
r = float(input('원의 반지름 : '))

calc_area(r)
print('원의 넓이 : ', area)