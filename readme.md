### �Ƴ��ܴ� 2020.02 / python 3.7
```bash
 https://www.anaconda.com/distribution/
```
 - Use Spyder

## ���̽㿡�� ����ϴ� ������ ����
 1. ����
 2. �Ǽ�
 3. ���ڿ�
 4. boolean

## ���Ĺ��� 
 1. %s : ���ڿ�
 2. %d : ����
 3. %f : �Ǽ�

## ����
 1. ���۷��� ����
   - �ּ� ����(C����� ������)
 2. ������ ����
   - ������ ����

## �Ҽ� ������ 
 - in : � �����Ͱ� Ư�� �����;ȿ� �����ϴ��� �˻�
         => ������� True �Ǵ� False
         => True : ������ False : �������� ����
      
 - not in : � �����Ͱ� Ư�� �����;ȿ� �����ϴ��� �ʴ��� �˻�
             => ������� True �Ǵ� False
             => True : �������� ���� False : ������
             
## ������ �ε���, �����̽�
 - 

## ���̵�ƼƼ ������

 - is : ���۷��� ������ �ּҰ��� ������ �˻�
        => ���� ����� True �Ǵ� False
        => True : ���۷��� ���� ����
            False : ���۷��� ���� �ٸ�
 - is not: ���۷��� ������ �ּҰ��� ���� ������ �˻�
        => ���� ����� True �Ǵ� False
        => True : ���۷��� ���� �ٸ�
             False : ���۷��� ���� ����
   
    ���۷���(reference) : ��ü�� ����Ű�� �ּҰ�
    ref(x)�� ���� main�Լ� �ȿ� �ִ� ����(x)�� ����Ű��
    ref �Լ������� �Ű����� n�� ���� ������ ���۷��� �� �� x�� �޴´�
    �̸� ���� ���� ����(pass-by-value)��� �θ���

```python
    def main():
        x = 1
        ref(x)
    def ref(n):
        n += 1
        print(n) => 2
```

## ���̽㿡�� ���� �ǹ�
 - ��ɾ���� ���� ����
 - ���(���ǹ�, �ݺ���) < �Լ� < Ŭ����

1. �ڹ�
```java
if(���ǽ�){
	��ɹ�;
}

int ex(){
          ��ɹ�;
}

class AAA{
	����;
	�Լ���
}
```
2. ���̽�: �鿩����
       - ���η� ���� ���̸�, ���� ��
       - ���� ������ : (�ݷ�)���� ����
```python
if(���ǽ�):
  ��ɹ�
  ��ɹ�

def main(�Ű�����):
  x = 1
  ��ɾ�
  
main()

class Ŭ������():
  ����
  ��ɾ�
```

```python
# ���� if else
if ���ǽ� :
    ��ɹ�
else: 
    if ���ǽ�:
        ��ɹ�
    else:
        if ���ǽ�:
            ��ɹ�
        else:
            ��ɹ�
```

## �ʱ� ������Ʈ ���������� API ���� pass�� ���� �������

## if ���� �����
```python
    year = int(input('�⵵ �Է� : '))
    
    if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
        print(str(year) + '���� �����Դϴ�.')
    else:
        print(str(year) + '���� ����Դϴ�.')
```

## ���� if-else�� : elif
```python
    score = int(input("���� �Է� : "))
    
    if score >= 90:
        print('A����')
    elif score >= 80:
        print('B����')
    elif score >= 70:
        print('C����')
    elif score >= 60:
        print('D����')
    else:
        print('F����')
```

## if ���� ����� ���: ���ڿ��� ȸ������ �ƴ��� ��� 
```bash
b='abcdefghijklmnopqrstuvwxyz'
print(b[1:15:1]) # ���ʿ��� ����������
print(b[15:1:-1]) # -�پ����� �����ʿ��� ��������
print(b[:])
print(b[::-1])
```
```python
a = 'abcdcba'
# (���๮�� ���϶� ) if(���ǽ�) (���๮�� ���� �ƴҶ�)
print(a, ': ȸ��' if a==a[::-1] else ':ȸ�� �ƴ�')
```

## �ݺ���
 - for��: Ƚ������ �ݺ�
 - while��: �������� �ݺ�
 
```python
for ���� in range(�ݺ�Ƚ��):
    ��ɹ�
for ���� in range(���۰�, ���ᰪ, ������):
    ��ɹ�
 # ��ȯ ���� ��ü: ���ڿ�, ����Ʈ, Ʃ��, ��ųʸ�, range()
for ���� in ���ڿ�:
 ��ɹ�
for ���� in ����Ʈ:
 ��ɹ�
for ���� in dict:
 ��ɹ�
```
## �ڷᱸ�� ������ �ڷ���
 1. ������ �ڷ���
   - ���ڿ�, Ʃ��, ����Ʈ
 2. ������� �ڷ���
   - ��Ʈ, ��ųʸ�

```bash
list = [1,2,3,4,5] # ������ ���� ����
tup1 = (1,2,3,4,5) # ������ ���� �Ұ���
tup2 = 1,2,3,4,5
set = {1,2,3,4,5} # ������ �ߺ� x
dic = {'a'=1, 'b'=2} # key:value ����
```
## �ڷ��� Unpacking
```bash
tup1 = (1,2,3,5)
print('{0} {1} {2} {3}'.format(*tup1))  # 1 2 3 4

dict = {'a'=1, 'b'=2}
print('{0} {1} {2} {3}'.format(*dict)  # a b
print('{} {} {} {}'.format(*dict))  # a b
print('{a} {b}'.format(**dict))  # 1 2
```

## List �޼ҵ� ����

```bash
list.index(data) # ����Ʈ�� �ִ� data��ġ�� �˷���
list.append(data) # ����Ʈ ���� �����͸� �߰��Ѵ�
list.sort(����, reverse=True) # ����Ʈ �����͸� �������� ���� / reverse=True �������� ����
list.pop() # ����Ʈ �� ������ ��Ҹ� �����ְ� �� ��Ҹ� �����Ѵ�
list.insert(��ġ��, data) # ����Ʈ�� Ư�� ��ġ�� ������ �����Ҽ��ִ�.
```
## List ������ ����
```python
list1 = [1,2,3]
print(list1)

# �ε������� ���� / ���� ������ ����
list1[2] = 40
print(list1)
list1[1] = ['a', 'b', 'c']
print(list1)

# �����̽����� ���� / ���� ������ ����
list1[1:2] = ['a', 'b', 'c']
print(list1)
list1.append('d')
print(list1)

list1[1:3] = 10,20
print(list1)
```

## List ������ ó��
```python
a = ['����', '����', '����', '��ȸ', '�ѱ�']
print(a)

a[3] = '����'
print(a)

a.append('�����')
print(a)

a.insert(2,'�Ϻ���')
print(a)

print('='*60)

# ���� : ���� ����Ʈ�� �ٲ��� ����
# ���̽� �����Լ� ���
print(sorted(a)) # �⺻: �������� ����
print(sorted(a, reverse=True)) # �������� ��
print(a)
print('='*60)

# ���� : ���� ����Ʈ�� �ٲ�
# ����Ʈ�� �����Լ� ���
a.sort() # �⺻ ��������
print(a)

a.sort(reverse=True) # ��������
print(a)

print('='*60)

# ����Ʈ ������ ����
# ���̽� �����Լ�
# �ε��� ���
del(a[4])
print(a)

# �����̽� ���
del(a[0:2])
print(a)

# ����Ʈ �����Լ�
# ����Ʈ �� ���� ������ ����
a.remove('����')
print(a)

# ����Ʈ �� ��� ������ ����
a.clear()
print(a)
```

## List ���� / ����Ʈ �ȿ� for�� �����ϱ�
```python
ex)
result = [0 for a in range(5)] # result = [ 0, 0, 0, 0, 0]
result = [num*3 for num in [1, 2, 3, 4] if num%2 == 0] # result = [6,12]
```

## Ʃ��(tuple)
```python
Ʃ��(tuple)�� �� ���� ���� �����ϰ� ����Ʈ�� ���� ����ϸ� ����Ʈ�� �ٸ� ���� ������ ����.
����Ʈ�� [ ]���� �ѷ������� Ʃ���� ( )���� �ѷ��Ѵ�.
����Ʈ�� �� ���� ����, ����, ������ ���������� Ʃ���� �� ���� �ٲ� �� ����.

tup1 = (1,2,3,4,5)
list1 = [10,20,30,40,50]

print("{} {} {} {}".format(*tup1))
print("{} {} {} {}".format(*list1))

print("{1} {2} {3} {4}".format(*tup1))
print("{4} {3} {2} {1}".format(*list1))

# �Ϲ� ������ Ʃ�� �����ϱ�
# unpacking : Ʃ���� ������ ������ ������ ������ �����ؾ��Ѵ�.
a,b,c,d,e=tup1
print(a,b,c,d,e)
```

## ��ųʸ�(Dict)
  - key�� value�� ���� / �ַ� Json ������ ó���Ҷ� ���� ��
```python
dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'���̽�'}
print(dict1)
print('='*60)

# indexing 
print(dict1['a'])
print(dict1['b'])
print(dict1['c'])
print(dict1['d'])
print('='*60)

# key���� �о����
dic_key = dict1.keys()
print(dic_key)

# value���� �о����
dic_value = dict1.values()
print(dic_value)

# key, value ������ �о����
dic_item = dict1.items()
print(dic_item)

# ������ �߰�
dict1['phone'] = '010-1234-5678'
print(dict1)

# ������ 1�� ����
del(dict1['b'])
print(dict1)

# ��� ������ ����
dict1.clear()
print(dict1)

# �⺻������ {} ���´� dict���·� �ν�������
# {} �ȿ� �ܼ� �����͵��� ��Ʈ�� �ν��ϰ�
# {key:value} key value ���´� dict ���·� �ν��Ѵ�.
test1 = {}
print(type(test1)) # dict

test2 = {1}
print(type(test2)) # set

test3 = {'a':'b'}  
print(type(test3)) # dict

dict1 = {'a':1, 'b':2, 'c':'Hello', 'd':'���̽�'}
print(dict1)
print('='*60)

# key�� ���� Ȯ��
print('c' in dict1)
print('Hello' in dict1)
print('='*60)

# data�� ���� Ȯ���� �ȵ�.

# ���� ������ Ȯ��
# 1. indexing ���
# 2. get() �Լ� ���
print(dict1['a'])
print(dict1.get('c'))
print('='*60)

print(dict1.get('f')) # ���� Ű�� ���� None ���
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

# ����
for key in sorted(dict1.keys(), reverse=True):
    print(key, dict1[key], end=', ')
    
print()
print('='*60)
# ������ ���� Ȯ��
print(len(dict1), '��')
print('='*60)
# ������ �߰�
# ������ 1�� �߰�
dict1['e'] = '������'
print(dict1)
print('='*60)

dict1.update({'f':'Java', 'g':'Spring'})
print(dict1)
print('='*60)
```

## ��Ʈ
```python
a = {1, 2, 3}
b = {1, 2, 3, 3}

print(a, len(a))
print(b, len(b))
print('='*60)

# ������ �߰�
a.add(5)
print(a, len(a))
print('='*60)

# ���� ������ Ȯ��
# �ε������� Ȯ�κҰ�
# print(a[0])

# 1. for�� ���
for v in a:
    print(v, end=', ')
print()
print('='*60)
# 2. .pop() ��� / Ȯ���� �����Ͱ� ������.
print(a, len(a))
print(a.pop())
print(a, len(a))
print('='*60)

# ������ ���� Ȯ��
print(2 in a)
print(2 not in a)
print('='*60)
```
## ���� ����� / with��
```python
with open("x.txt") as f:
    data = f.read()
    do something
```

## ���̽� Ŭ����
```python
class HelloWorld:
    message = 0                       # Ŭ���� ����
    
    def setEng(self):
        self.message = 'Hello Python' # �ν��Ͻ� ����
        
    def setKor(self):
        self.message = '�ȳ��ϼ���. ���̽�'
        
    def setKor2(self):
        message = '���̽� ������'     #��������
        
    def sayHello(self):
        print(self.message)
```

# ���̽� Ŭ���� ���ۿ���
```bash
1. Java�� this�� ����(Ȥ�� ����)
2. ������

```
```python
class Score:
    def set(self):
        print(self)
        self.num = int(input('�й� : '))
        self.name = input('�̸� : ')
        self.kor = int(input('���� : '))
        self.eng = int(input('���� : '))
        self.mat = int(input('���� : '))
        self.tot = self.kor + self.eng + self.mat
        self.avg = self.tot / 3
        
        
    def output_title(self):
        print(self)
        print('***�������***')
        print('%3s %6s %3s %3s %3s %3s %3s' %(
            '�й�', '�̸�', '����', '����', '����', '����', '���'))
        
        
    def output(self):
        print(self)
        print('%3s %6s %3s %3s %3s %3s %3s' %(self.num, self.name, 
                self.kor, self.eng, self.mat, self.tot, self.avg))
        
        
s1 = Score()
s2 = Score()


print('s1=', s1)
print('s2=', s2)
print('-'*60)

s1.set()  # s1.set(s1) : ����Լ��� ȣ���ϸ�, ȣ���ϴ� ��ü�� ����
s2.set()

```
## ������
## Ŭ���� ����� ��������
 - ���̽㿡���� �⺻������ public���� �����Ǿ��ִ�.
 - ��� ������ private���� �����ϴ� ���
```python
__name # Ŭ���� �ȿ��� �ܺη� ������� �ʴ� �̸����� �ν�
__name__ # �յڷ�__�� �پ��ִ� �̸��� �ý��ۿ��� ������ �̸�
```
## getter / setter
 - getter : ������� �տ� get�� �ٿ��� ���� �Լ� / ��������� ����
 - setter : ������� �տ� set�� �ٿ��� ���� �Լ� / ��������� �� ����
```python
class Triangle():
    # ������
    def __init__(self, high=0, under=0): # �Ű����� 2���� �ʱ�ȭ��Ű��
        self.high = high # �Ű����� �Ҵ�
        self.under = under # �Ű����� �Ҵ�
        
    # �ﰢ�� ���� ����
    # setter
    def setTriangle(self, high, under): # �����͸� ������ �Ű����� �ΰ��� �ް�
        self.high = high # �Ҵ�
        self.under = under # �Ҵ�
      
    # �غ� ���� ����
    # getter
    def getArea(self):
        return self.high * self.under
        
t1 = Triangle(45, 7) # t1.__init__(45,7)
print(t1.getArea())

t2 = Triangle(5,3)  # t2.__init__(5,3)
print(t2.getArea())

```
 
## __str__
 - ��ü���� print()�� ����ϸ� �ڵ� ȣ��Ǵ� �޼ҵ�
```python
class Car :
    def __init__(self, speed=0, color=0, model=0):
        print('__init__ȣ��')
        self.speed = speed
        self.color = color
        self.model = model
        
    # �Ϲ������� ��� ��������� Ȯ���ϴ� �뵵�� ���� ���
    def __str__(self):
        print('__str__ȣ��')
        return ('�ӵ�: {}, ����:{}, ��:{}'.format(self.speed, 
                                                    self.color, self.model))    

    def drive(self, speed):
        self.speed = speed
        
car = Car(0, 'blue', 'E-Class')
print(car)
print('-'*30)
print(car.__str__())
print('-'*30)

# ���� ���
'''
__init__ȣ��
__str__ȣ��
�ӵ�: 0, ����:blue, ��:E-Class
------------------------------
__str__ȣ��
�ӵ�: 0, ����:blue, ��:E-Class
------------------------------
'''
```

## ���

```python
class Article:
    
    def __init__(self):
        self.num = 0
        self.title = 0
        
        
class FileArticle(Article):
    
    def __init__(self):
        self.fileName = 0
        
    def __str__(self):
        return '�ڷ�� [��ȣ= {}, ����={}, ÷������={}'.format(
                self.num, self.title, self.fileName)
    

class QNAArticle(Article):
    
    def __init__(self):
        self.answer = 0
    
    def __str__(self):
        return '����/�亯 [�۹�ȣ={}, ����={}, �亯={}'.format(
            self.num, self.title, self.answer)
    
fileArticle = FileArticle()
fileArticle.num = 1
fileArticle.title = 'ù��° �ڷ��Դϴ�.'
fileArticle.fileName = 'python.ppt'
print(fileArticle) # fileArticle.__str__()
print('-'*30)

qna = QNAArticle()
qna.num = 1
qna.title = 'ù��° �����Դϴ�.'
qna.answer = 'ù��° �亯�Դϴ�.'
print(qna)
print('-'*30)

```
