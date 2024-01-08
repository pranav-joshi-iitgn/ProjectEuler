def check(a,b,c):
    n = a*(9091) + b*(910) + c*(100)
    for x in range(10,91):
        if n%x == 0:
            if n//x > 99 and n//x < 1000:
                return 11*x
    return False
        
con = True
for a in range(9,0,-1):
    for b in range(9,-1,-1):
        for c in range(9,-1,-1):
            x = check(a,b,c) 
            if x :
                print(a*(100001) + b*(10010) + c*(1100),x)
                con = False
                break
        if not con :
            break
    if not con :
        break