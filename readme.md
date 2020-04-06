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
        