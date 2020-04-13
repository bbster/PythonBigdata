### 아나콘다 2020.02 / python 3.7
```bash
 https://www.anaconda.com/distribution/
```
 - Use Spyder

## 파이썬에서 사용하는 데이터 형식
 1. 정수
 2. 실수
 3. 문자열
 4. boolean

## 서식문자 
 1. %s : 문자열
 2. %d : 정수
 3. %f : 실수

## 변수
 1. 레퍼런스 변수
   - 주소 저장(C언어의 포인터)
 2. 데이터 변수
   - 데이터 저장

## 소속 연산자 
 - in : 어떤 데이터가 특정 데이터안에 존재하는지 검사
         => 결과값은 True 또는 False
         => True : 존재함 False : 존재하지 않음
      
 - not in : 어떤 데이터가 특정 데이터안에 존재하는지 않는지 검사
             => 결과값은 True 또는 False
             => True : 존재하지 않음 False : 존재함
             
## 데이터 인덱싱, 슬라이싱
 - 

## 아이덴티티 연산자

 - is : 레퍼런스 변수의 주소값이 같은지 검사
        => 연산 결과는 True 또는 False
        => True : 레퍼런스 값이 같음
            False : 레퍼런스 값이 다름
 - is not: 레퍼런스 변수의 주소값이 같지 않은지 검사
        => 연산 결과는 True 또는 False
        => True : 레퍼런스 값이 다름
             False : 레퍼런스 값이 같음
   
    레퍼런스(reference) : 객체를 가르키는 주소값
    ref(x)를 통해 main함수 안에 있는 인자(x)를 가르키고
    ref 함수에서는 매개변수 n을 통해 인자의 레퍼런스 값 즉 x를 받는다
    이를 값에 의한 전달(pass-by-value)라고 부른다

```python
    def main():
        x = 1
        ref(x)
    def ref(n):
        n += 1
        print(n) => 2
```

## 파이썬에서 블럭의 의미
 - 명령어들을 묶는 단위
 - 제어문(조건문, 반복문) < 함수 < 클래스

1. 자바
```java
if(조건식){
	명령문;
}

int ex(){
          명령문;
}

class AAA{
	변수;
	함수들
}
```
2. 파이썬: 들여쓰기
       - 세로로 같은 줄이면, 같은 블럭
       - 블럭의 시작은 : (콜론)으로 시작
```python
if(조건식):
  명령문
  명령문

def main(매개변수):
  x = 1
  명령어
  
main()

class 클래스명():
  변수
  명령어
```

```python
# 다중 if else
if 조건식 :
    명령문
else: 
    if 조건식:
        명령문
    else:
        if 조건식:
            명령문
        else:
            명령문
```

## 초기 프로젝트 구조잡을때 API 명명과 pass를 통해 구조잡기

## if 삼항 연산식
```python
    year = int(input('년도 입력 : '))
    
    if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
        print(str(year) + '년은 윤년입니다.')
    else:
        print(str(year) + '년은 평년입니다.')
```

## 다중 if-else문 : elif
```python
    score = int(input("점수 입력 : "))
    
    if score >= 90:
        print('A학점')
    elif score >= 80:
        print('B학점')
    elif score >= 70:
        print('C학점')
    elif score >= 60:
        print('D학점')
    else:
        print('F학점')
```

## if 삼향 연산식 사용: 문자열이 회문인지 아닌지 출력 
```bash
b='abcdefghijklmnopqrstuvwxyz'
print(b[1:15:1]) # 왼쪽에서 오른쪽으로
print(b[15:1:-1]) # -붙었을때 오른쪽에서 왼쪽으로
print(b[:])
print(b[::-1])
```
```python
a = 'abcdcba'
# (실행문이 참일때 ) if(조건식) (실행문이 참이 아닐때)
print(a, ': 회문' if a==a[::-1] else ':회문 아님')
```

## 반복문
 - for문: 횟수제어 반복
 - while문: 조건제어 반복
 
```python
for 변수 in range(반복횟수):
    명령문
for 변수 in range(시작값, 종료값, 증감값):
    명령문
 # 순환 가능 객체: 문자열, 리스트, 튜플, 딕셔너리, range()
for 변수 in 문자열:
 명령문
for 변수 in 리스트:
 명령문
for 변수 in dict:
 명령문
```
## 자료구조 데이터 자료형
 1. 순서형 자료형
   - 문자열, 튜플, 리스트
 2. 비순서형 자료형
   - 세트, 딕셔너리

```bash
list = [1,2,3,4,5] # 데이터 변경 가능
tup1 = (1,2,3,4,5) # 데이터 변경 불가능
tup2 = 1,2,3,4,5
set = {1,2,3,4,5} # 데이터 중복 x
dic = {'a'=1, 'b'=2} # key:value 형식
```
## 자료형 Unpacking
```bash
tup1 = (1,2,3,5)
print('{0} {1} {2} {3}'.format(*tup1))  # 1 2 3 4

dict = {'a'=1, 'b'=2}
print('{0} {1} {2} {3}'.format(*dict)  # a b
print('{} {} {} {}'.format(*dict))  # a b
print('{a} {b}'.format(**dict))  # 1 2
```

## List 메소드 사용법

```bash
list.index(data) # 리스트에 있는 data위치를 알려줌
list.append(data) # 리스트 끝에 데이터를 추가한다
list.sort(변수, reverse=True) # 리스트 데이터를 오름차순 정렬 / reverse=True 내림차순 정렬
list.pop() # 리스트 맨 마지막 요소를 돌려주고 그 요소를 삭제한다
list.insert(위치값, data) # 리스트에 특정 위치에 데이터 삽입할수있다.
```
## List 데이터 변경
```python
list1 = [1,2,3]
print(list1)

# 인덱싱으로 변경 / 단일 데이터 변경
list1[2] = 40
print(list1)
list1[1] = ['a', 'b', 'c']
print(list1)

# 슬라이싱으로 변경 / 복수 데이터 변경
list1[1:2] = ['a', 'b', 'c']
print(list1)
list1.append('d')
print(list1)

list1[1:3] = 10,20
print(list1)
```

## List 데이터 처리
```python
a = ['국어', '영어', '수학', '사회', '한국']
print(a)

a[3] = '과학'
print(a)

a.append('세계사')
print(a)

a.insert(2,'일본어')
print(a)

print('='*60)

# 정렬 : 원본 리스트는 바뀌지 않음
# 파이썬 내장함수 사용
print(sorted(a)) # 기본: 오름차순 정렬
print(sorted(a, reverse=True)) # 내림차순 정
print(a)
print('='*60)

# 정렬 : 원본 리스트는 바뀜
# 리스트의 내장함수 사용
a.sort() # 기본 오름차순
print(a)

a.sort(reverse=True) # 내림차순
print(a)

print('='*60)

# 리스트 데이터 삭제
# 파이썬 내장함수
# 인덱싱 방법
del(a[4])
print(a)

# 슬라이싱 방법
del(a[0:2])
print(a)

# 리스트 내장함수
# 리스트 내 단일 데이터 삭제
a.remove('영어')
print(a)

# 리스트 내 모든 데이터 삭제
a.clear()
print(a)
```

## List 내포 / 리스트 안에 for문 포함하기
```python
ex)
result = [0 for a in range(5)] # result = [ 0, 0, 0, 0, 0]
result = [num*3 for num in [1, 2, 3, 4] if num%2 == 0] # result = [6,12]
```

## 튜플(tuple)
```python
튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

tup1 = (1,2,3,4,5)
list1 = [10,20,30,40,50]

print("{} {} {} {}".format(*tup1))
print("{} {} {} {}".format(*list1))

print("{1} {2} {3} {4}".format(*tup1))
print("{4} {3} {2} {1}".format(*list1))

# 일반 변수에 튜플 저장하기
# unpacking : 튜플의 데이터 개수와 변수의 개수가 동일해야한다.
a,b,c,d,e=tup1
print(a,b,c,d,e)
```

## 딕셔너리(Dict)
  - key와 value로 저장 / 주로 Json 데이터 처리할때 많이 씀
```python
dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dict1)
print('='*60)

# indexing 
print(dict1['a'])
print(dict1['b'])
print(dict1['c'])
print(dict1['d'])
print('='*60)

# key값만 읽어오기
dic_key = dict1.keys()
print(dic_key)

# value값만 읽어오기
dic_value = dict1.values()
print(dic_value)

# key, value 쌍으로 읽어오기
dic_item = dict1.items()
print(dic_item)

# 데이터 추가
dict1['phone'] = '010-1234-5678'
print(dict1)

# 데이터 1개 삭제
del(dict1['b'])
print(dict1)

# 모든 데이터 삭제
dict1.clear()
print(dict1)

# 기본적으로 {} 형태는 dict형태로 인식하지만
# {} 안에 단순 데이터들은 세트로 인식하고
# {key:value} key value 형태는 dict 형태로 인식한다.
test1 = {}
print(type(test1)) # dict

test2 = {1}
print(type(test2)) # set

test3 = {'a':'b'}  
print(type(test3)) # dict

dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dict1)
print('='*60)

# key값 유무 확인
print('c' in dict1)
print('Hello' in dict1)
print('='*60)

# data값 유무 확인은 안됨.

# 개별 데이터 확인
# 1. indexing 방법
# 2. get() 함수 사용
print(dict1['a'])
print(dict1.get('c'))
print('='*60)

print(dict1.get('f')) # 없는 키값 사용시 None 출력
print('='*60)

# for
for key in dict1.keys():
    print(key, end=', ')

print()
print('='*60)

for value in dict1.values():
    print(value, end=', ')

print()
print('='*60)

for key, value in dict1.items():
    print(key, value, end=', ')
    
print()
print('='*60)

# 정렬
for key in sorted(dict1.keys(), reverse=True):
    print(key, dict1[key], end=', ')
    
print()
print('='*60)
# 데이터 갯수 확인
print(len(dict1), '개')
print('='*60)
# 데이터 추가
# 데이터 1개 추가
dict1['e'] = '빅데이터'
print(dict1)
print('='*60)

dict1.update({'f':'Java', 'g':'Spring'})
print(dict1)
print('='*60)
```

## 세트
```python
a = {1, 2, 3}
b = {1, 2, 3, 3}

print(a, len(a))
print(b, len(b))
print('='*60)

# 데이터 추가
a.add(5)
print(a, len(a))
print('='*60)

# 개별 데이터 확인
# 인덱싱으로 확인불가
# print(a[0])

# 1. for문 사용
for v in a:
    print(v, end=', ')
print()
print('='*60)
# 2. .pop() 사용 / 확인한 데이터가 삭제됨.
print(a, len(a))
print(a.pop())
print(a, len(a))
print('='*60)

# 데이터 유무 확인
print(2 in a)
print(2 not in a)
print('='*60)
```
## 파일 입출력 / with문
```python
with open("x.txt") as f:
    data = f.read()
    do something
```

## 파이썬 클래스
```python
class HelloWorld:
    message = 0                       # 클래스 변수
    
    def setEng(self):
        self.message = 'Hello Python' # 인스턴스 변수
        
    def setKor(self):
        self.message = '안녕하세요. 파이썬'
        
    def setKor2(self):
        message = '파이썬 파이팅'     #지역변수
        
    def sayHello(self):
        print(self.message)
```

# 파이썬 클래스 동작원리
```bash
1. Java의 this와 유사(혹은 동일)
2. 생성자

```
```python
class Score:
    def set(self):
        print(self)
        self.num = int(input('학번 : '))
        self.name = input('이름 : ')
        self.kor = int(input('국어 : '))
        self.eng = int(input('영어 : '))
        self.mat = int(input('수학 : '))
        self.tot = self.kor + self.eng + self.mat
        self.avg = self.tot / 3
        
        
    def output_title(self):
        print(self)
        print('***성정출력***')
        print('%3s %6s %3s %3s %3s %3s %3s' %(
            '학번', '이름', '국어', '영어', '수학', '총점', '평균'))
        
        
    def output(self):
        print(self)
        print('%3s %6s %3s %3s %3s %3s %3s' %(self.num, self.name, 
                self.kor, self.eng, self.mat, self.tot, self.avg))
        
        
s1 = Score()
s2 = Score()


print('s1=', s1)
print('s2=', s2)
print('-'*60)

s1.set()  # s1.set(s1) : 멤버함수를 호출하면, 호출하는 객체가 전달
s2.set()

```
## 생성자
## 클래스 멤버의 접근제한
 - 파이썬에서는 기본적으로 public으로 설정되어있다.
 - 멤버 변수를 private으로 설정하는 방법
```python
__name # 클래스 안에서 외부로 노출되지 않는 이름으로 인식
__name__ # 앞뒤로__가 붙어있는 이름은 시스템에서 정의한 이름
```
## getter / setter
 - getter : 멤버변수 앞에 get을 붙여서 만든 함수 / 멤버변수값 리턴
 - setter : 멤버변수 앞에 set을 붙여서 만듬 함수 / 멤버변수에 값 저장
```python
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

```
 
## __str__
 - 객체명을 print()로 출력하면 자동 호출되는 메소드
```python
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

# 실행 결과
'''
__init__호출
__str__호출
속도: 0, 색상:blue, 모델:E-Class
------------------------------
__str__호출
속도: 0, 색상:blue, 모델:E-Class
------------------------------
'''
```

## 상속

```python
class Article:
    
    def __init__(self):
        self.num = 0
        self.title = 0
        
        
class FileArticle(Article):
    
    def __init__(self):
        self.fileName = 0
        
    def __str__(self):
        return '자료실 [번호= {}, 제목={}, 첨부파일={}'.format(
                self.num, self.title, self.fileName)
    

class QNAArticle(Article):
    
    def __init__(self):
        self.answer = 0
    
    def __str__(self):
        return '질문/답변 [글번호={}, 제목={}, 답변={}'.format(
            self.num, self.title, self.answer)
    
fileArticle = FileArticle()
fileArticle.num = 1
fileArticle.title = '첫번째 자료입니다.'
fileArticle.fileName = 'python.ppt'
print(fileArticle) # fileArticle.__str__()
print('-'*30)

qna = QNAArticle()
qna.num = 1
qna.title = '첫번째 질문입니다.'
qna.answer = '첫번째 답변입니다.'
print(qna)
print('-'*30)

```
