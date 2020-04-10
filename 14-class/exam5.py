def plus(x,y):
    print('함수 plus() 호출')
    return x+y


class Calc :
        def plus(self, x, y):
            print('메서드 plus() 호출')
            return x+y
    
    
        def minus(self, x,y):
            return x-y

        
        def multiply(self,x,y):
            return x*y
        
        
        def divide(self,x,y,):
            return x/y
        
        
        def f(self,x,y):
            result1 = plus(x,y)
            result2 = self.plus(x,y)
            result3 = result1+result2
            return result3


c = Calc()
p = c.plus(100,50)
print(p)

print(c.minus(100,50))
print(c.multiply(100,50))
print(c.divide(100,50))
print(c.f(100,50))
