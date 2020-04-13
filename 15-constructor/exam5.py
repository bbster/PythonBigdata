from random import random
from random import randint
from random import randrange
from random import sample

# 0.0 ~ 1.0 미만의 임의 실수값 1개 생성
print(random())

# randint(시작,끝) 시작~끝 사이의 임의 정수값 1개 생성
print(randint(0,9))

# randrange(시작,끝,스탭값) 시작~끝 사이의 임의 정수값 1개 생성
# 스탭값 설정 가능
print(randrange(0,10))

print(chr(randint(65, 90)))
print(chr(randint(97, 122)))

# 리스트에서 임의값을 선택 추출
print(sample([1,2,3,4,5], 2))

li = [x for x in range(1, 46)]
print(li)
print(sample(li, 6))
