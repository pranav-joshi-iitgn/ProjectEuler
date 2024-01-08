
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
        if r == 0:
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
    return x,y  
def CRT(r1,p1,r2,p2):
    x,_ = dio(p1,-p2,r2-r1)
    return (r1 + p1*x)%(p1*p2)
def fastExp(x,n,m=None):
    L = []
    while n > 0:
        L.append(n%2)
        n = n//2
    P = 1
    for i in range(len(L)):
        if(L[i]):
            P *= x
        x = x*x
        if not m is None:
            x = x%m
            P = P%m
    return P
    

E = 10
N = 1001
R = []
for p in [2,5]:
    d = p**E
    t = (p-1)*(p**(E-1))
    I = [1]*N
    In = [0]*N
    pow = p
    while pow < N:
        for i in range(pow,N,pow):
            I[i] = pow
            In[i] += 1
        pow *= p

    NI = [(i//I[i])%d for i in range(N)]
    
    for i in range(N):
        if In[i]*i >= E:
            I[i] = 0

    P = [i%t for i in range(N)]
    L = [fastExp(NI[i],P[i],d) for i in range(N)]

    L = [(L[i]*(fastExp(I[i],i,d)))%d for i in range(N)]

    S = 0
    for i in range(1,N):
        S += L[i]
        S = S%d
    R.append(S)

print(R)
print(CRT(R[0],2**E,R[1],5**E))


