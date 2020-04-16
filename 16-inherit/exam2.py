class CalcParent1:
    
    def __init__(self):
        self.aa = 5
        self.bb = 7

    def plus(self, x, y):
        return x+y
    
    def minus(self, x, y):
        return x-y
    
class CalcParent2:
    
    def __init__(self):
        self.aa2 = 50
        self.bb2 = 70

    def plus2(self, x, y):
        return x+y+1
    
    def minus2(self, x, y):
        return x-y-1
    
class CalcChild(CalcParent1, CalcParent2): # 부모클래스 상속받음

    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
cp = CalcParent1()
cp = CalcParent2()
cc = CalcChild()

print(cc.plus(200,100))
print(cc.minus(200,100))
print(cc.plus2(200,100))
print(cc.minus2(200,100))
print(cc.multiply(200,100))
print(cc.divide(200,100))
print('-'*30)

print(cc.aa)
print(cc.bb)
