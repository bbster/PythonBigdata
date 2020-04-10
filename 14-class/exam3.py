class Character :
    name = 0  # 클래스 변수
    age = 0
    
d = Character()
d.name = '홍길동' # 인스턴스 변
d.age = 24
print('이름:', d.name, '/ 나이:', d.age)
print('이름:', Character.name, '/ 나이:', Character.age)
print('-'*30)

Character.name = 'TFT모바일'
Character.age = '1'
print('이름:', Character.name, '/ 나이:', Character.age)
print('-'*30)
h = Character()
h.name = '희동'
h.age = 3
print('이름:', h.name, '/ 나이:', h.age)
print('-'*30)   