class Car :
    def __init__(self, speed=0, color=0, model=0):
        print('__init__호출')
        self.speed = speed
        self.color = color
        self.model = model
        
    # 일반적으로 모든 멤버변수를 확인하는 용도로 많이 사용
    def __str__(self):
        print('__str__호출')
        return ('속도: {}, 색상:{}, 모델:{}'.format(self.speed, 
                                                    self.color, self.model))    

    def drive(self, speed):
        self.speed = speed
        
car = Car(0, 'blue', 'E-Class')
print(car)
print('-'*30)
print(car.__str__())

print('-'*30)