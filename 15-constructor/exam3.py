class Member():
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age = age
        
mem = Member()
print(mem.getName())
print(mem.getAge())

mem.setName('홍길동')
mem.setAge(25)
print(mem.getName())
print(mem.getAge())

# 인스턴스 변수 추가
# -> 클래스 밖에서는 __를 붙여도 public으로 동작함
mem.__name = '이영희'
mem.__age = 30
print(mem.__name)
print(mem.__age)
print('-'*30)