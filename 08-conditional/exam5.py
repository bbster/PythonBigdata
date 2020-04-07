# 회문 : 왼쪽에서 읽었을때와 오른쪽에서 읽었을 때 같은 문자열
def exam5():
    a = 'abcdcba'
    #print(a, ': 회문' if a==a[::-1] else ':회문 아님')
    
    b='abcdefghijklmnopqrstuvwxyz'
    print(b[1:15:1]) # 왼쪽에서 오른쪽으로
    print(b[15:1:-1]) # -붙었을때 오른쪽에서 왼쪽으로 
    print(b[:])
    print(b[::-1])
    
    
exam5()