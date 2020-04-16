import string

st1 = string.ascii_letters + string.digits
print(st1)

# 입력 값 valid()
while True:
    userId = input('your id : ')
    
    for ch in userId :
        if ch not in st1 :
            print('invalid user id')
            checkId = False
            break
        else: checkId = True
        
    if checkId:
        print('valid user id')
        break
