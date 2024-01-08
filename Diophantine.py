def LCfor1(a,b):
    n = a
    d = b
    xd = 1
    yd = 0
    xr = 0
    yr = 1

    while True:
        r = n%d
        q = n//d
        xrn = xd - q*xr
        yrn = yd - q*yr
        xd = xr
        yd = yr
        xr = xrn
        yr = yrn
        print(d,' = (',xd,')*',a,' + (',yd,')*',b,sep='')
        if r == 0:
            print('gcd : ',d)
            break
        n = d
        d = r
    
    return xd,yd,d

def dio(a,b,c):
    x,y,g = LCfor1(a,b)
    if c % g != 0:
        print('Not possible')
        return None,None
    x = (c//g)*x
    y = (c//g)*y
    a = a//g
    b = b//g
    while True:
        if x > b:
            x = x-b
            y = y+a
        elif x < -b:
            x += b
            y += -a
        else:
            break
    a = a*g
    b = b*g
    print(c,'=',x,'*',a,'+',y,'*',b)
    return x,y
    
phi = 4*(5**9)
ex = 7830457 % phi
N = (28433*(2**ex)+1) % (5**10)
N += -1
print(N)
a = 5**10
b = 2**10
x,y = dio(-a,b,N)

print(N + a*x + 1)

    


