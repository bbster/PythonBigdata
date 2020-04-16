tot = 0

for a in range(1, 101):
    tot += a
    if a%10==1: print('%2d ~ ' %a, end='')
    if a%10==0: 
        print('%3d = %3d' %(a, tot))
        tot = 0
    