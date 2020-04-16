class Car:
    speed = 5  # 클래스 변수
    
    def drive(self):
        self.speed  = 10  # 인스턴스 변수
        
        
    def output(self):
        print('Car.speed=', Car.speed)
        print('self.speed=', self.speed)
        
print(Car.speed)

myCar = Car()
myCar.output()

myCar.drive()
myCar.output()
