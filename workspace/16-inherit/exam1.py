class CalcParent:

    def plus(self, x, y):
        return x+y
    
    def minus(self, x, y):
        return x-y
    
class CalcChild(CalcParent): # 부모클래스 상속받음
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
cp = CalcParent()
cc = CalcChild()

print(cc.plus(10,2)) # 부모클래스에 있는 함수 사용가능
print(cc.minus(10,2))
print(cc.multiply(10,2))
print(cc.divide(10,2))
    