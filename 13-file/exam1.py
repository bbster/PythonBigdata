# 파일 열기
f = open('test.txt', 'wb ') # 쓰기모드

# 파일 데이터 저장
for i in range(1, 11):
    data = str(i) + '번째 줄입니다. \n'
    f.write(data)
    
# 파일 닫기
f.close()
    

