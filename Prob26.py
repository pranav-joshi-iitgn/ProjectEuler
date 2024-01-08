from math import gcd
def index(a,n,m):
    x = a
    i = 1
    while i < n:
        if(x==1):
            return i
        x = (a*x)%m
        i += 1
    return 0

lrc = 1
d = 1
for m in range(2,1000):
    if(gcd(10,m)>1):
        continue
    i = index(10,m,m)
    if(i>lrc):
        lrc = i
        d = m
print(lrc,d)