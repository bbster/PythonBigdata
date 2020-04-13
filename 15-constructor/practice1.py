class Triangle():
    # 생성자
    def __init__(self, high=0, under=0): # 매개변수 2개를 초기화시키고
        self.high = high # 매개변수 할당
        self.under = under # 매개변수 할당
        
    # 삼각형 넓이 리턴
    # setter
    def setTriangle(self, high, under): # 데이터를 저장할 매개변수 두개를 받고
        self.high = high # 할당
        self.under = under # 할당
      
    # 밑변 높이 대입
    # getter
    def getArea(self):
        return self.high * self.under
        
t1 = Triangle(45, 7) # t1.__init__(45,7)
print(t1.getArea())

t2 = Triangle(5,3)  # t2.__init__(5,3)
print(t2.getArea())
