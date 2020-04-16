def practice1():
    stadium = input('경기장은 어디입니까? ')
    
    winner = input('이긴팀은 어디입니까?')
    
    looser = input('진팀은 어디입니까?')
    
    score = input('몇대몇입니까?')
    
    print('오늘 %s에서 야구경기가 열렸습니다.' %stadium)
    print('삼성과 LG의 치열한 공방전을 펼쳤습니다.')
    print('결국 %s은 %s를 %s로 이겼습니다.' %(winner ,looser, score))
    print('-'*134)
    print('''\
          ==============================================
          오늘 %s에서 야구경기가 열렸습니다.
          %s과 %s의 치열한 공방전을 펼쳤습니다.
          결국 %s은 %s를 %s로 이겼습니다.
          ==============================================
          ''' %(stadium, winner, looser, winner, looser, score))
practice1()
    