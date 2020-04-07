def exam3():

    for x in range(2,10):
        print()
        for y in range(1,10):
            result = x * y
            # 자동으로\n 들어가고있음
            print('%d*%d=%2d' %(x,y,result), end=" ")
    

        
exam3()