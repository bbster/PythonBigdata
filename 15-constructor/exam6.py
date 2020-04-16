from random import random
from random import sample


class Lotto():
    def __init__(self, li=[], num=0):
        self.li = li
        self.num = int(input('구매횟수를 입력하세요 : '))       
        
    # 로또번호 생성
    def lottonum(self):
        self.li = [x for x in range(1, 46)]
        
        
    # 로또번호 정렬
    def lottosort(self):
        self.lottoprint()

    # 로또번호 출력
    def lottoprint(self):
         for x in range(self.num):
            print('번호 : ', sample(self.li, 6))
        
lotto = Lotto()
lotto.lottonum()
lotto.lottosort()


'''
import random
class Lotto:
    def __init__(self) :
        self.m = 0
        self.buyNum = 0
        
    def inputBuyNum(self):
        self.buyNum = int(input('구매횟수를 입력하세요 : '))
        print()
        
    def selectLotto(self):
        for i in range(self.buyNum):
            self.m = random.sample([a for a in range(1, 46)], 6)
            self.m.sort()
            self.outputResult()
            
    def outputResult(self):
        print('%2d %2d %2d %2d %2d %2d' %(self.m[0], self.m[1], self.m[2],
        self.m[3], self.m[4],self.m[5],))
        
    
'''