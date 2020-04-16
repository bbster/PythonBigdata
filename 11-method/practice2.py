def grade(avg):

    if avg >= 90 and avg <= 100:
        return 'A'
    elif avg >= 80 and avg <=89:
        return 'B'
    elif avg >= 70 and avg <=79:
        return 'C'
    elif avg >= 60 and avg <=69:
        return 'D'
    else :
        return 'F'


def calc(x,y):
    total = x + y
    avg = total / 2
    return avg


def output(avg):
    print(grade(avg), '학점입니다')
    
    
def main():
    x = int(input('국어 점수 입력 : '))
    y = int(input('영어 점수 입력 : '))

    avg = calc(x, y)
    output(avg)
    
main()
