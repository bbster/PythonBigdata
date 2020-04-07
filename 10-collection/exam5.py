def exam5():
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
    
exam5()
