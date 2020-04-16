def total(*args):
    tot = 0
    for x in args:
        tot += x
    return tot
    
    
print(total(2, 3, 4, 5, 6, 7))
print(total(20, 30, 40))