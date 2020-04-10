class Calcurator:
        def plus(self, x, y):
            return x+y
    
    
        def minus(self, x,y):
            return x-y
    
    
        def multiply(self,x,y):
            return x*y

        
        def divide(self,x,y,):
            return x/y

        # 클래스 안의 메소드에서 다른 메소드를 사용할 때는
        # 반드시 self를 붙여서 사용 해야 한다.       
        def f(self,x,y):
            return self.plus(x,y) + self.multiply(x,y)
        