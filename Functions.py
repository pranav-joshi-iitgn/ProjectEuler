def LCforGcd(a,b):
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
def gcd(a,b):
    return LCforGcd(a,b)[-1]
def lcm(a,b):
    return a*(b//gcd(a*b))
def dio(a,b,c):
    x,y,g = LCforGcd(a,b)
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
def PF(n):
    D = {}
    x = 2
    while n != 1:
        if n%x == 0:
            if x in D :
                D[x] += 1
            else :
                D[x] = 1
            n = n//x
        else :
            if x*x > n :
                D[n] = 1
                break
            x += 1
    return D
def Sig(n):
    D = {}
    x = 2
    while x*x <= n:
        if(n%x==0):
            if(x in D):
                D[x] += 1
            else:
                D[x] = 1
            n = n//x
        else:
            x += 1
    if(n!=1):
        if(n in D):
            D[n] += 1
        else:
            D[n] = 1

    P = 1
    for x in D :
        P *= (x**(D[x]+1) -1)//(x-1)
    del D
    return P
def generatePrimes(N):
    L = [True]*(N+1)
    L[0] = False
    L[1] = False
    primes = []
    for i in range(2,N+1):
        if(L[i]):
            primes.append(i)
            j = 2*i
            while j <= N :
                L[j] = False
                j += i
    return primes
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
def multiples(l,m):
    a = l[0]
    b = l[1]
    if a <= m :
        a += m
    if b < a :
        return 0
    if(a%m):
        a = a//m + 1
    else:
        a = a//m
    b = b//m        
    return b - a + 1
def divByAll(L):
    if len(L) == 1:
        return 99
    if len(L) == 0:
        return 0
    m = lcm(L[0],L[1])
    for i in range(2,len(L)):
        m = lcm(m,L[i])
    a = min(L)
    b = a*100
    return multiples([a,b],m) 
def subsets(n,size):
    if n == size :
        return [list(range(1,n+1))]
    if n < size :
        return []
    if size == 1 :
        return [[x] for x in range(1,n+1)]
    l1 = subsets(n-1,size)
    l2 = subsets(n-1,size-1)
    for l in l2:
        l.append(n)
    return l1 + l2
def one(N):
    S = 0
    sig = 1
    for size in range(1,N+1):
        for s in subsets(N,size):
            S += sig * all(s)
        sig = - sig
    return S 
def isPrime(x):
    if x<=1:
        return False
    if x==2:
        return True
    if x%2 == 0:
        return False
    m = int(x**0.5)
    for i in range(3,m+2):
        if x%i == 0:
            return False
    return True
def isLeftTruncable(x):
    s = str(x)
    for i in range(len(s)):
        x = int(s[i:])
        if not isPrime(x):
            return False
    return True
def incSeq(low,high,size):
    if high < low :
        return []
    if size <= 0:
        return []
    if size==1:
        return list(map(str,range(low,high+1)))
    L = []
    for i in range(low,high+1):
        l = incSeq(i,high,size-1)
        for j in range(len(l)):
            l[j] = str(i) + l[j]
        L += l
    return L
def perm(s,stop=5,lev=0):
    if lev >= stop :
        return ['']
    l = len(s)
    if(l<=1):
        return [s]
    toRet = []
    for i in range(l):
        c = s[i]
        L = perm(s[:i]+s[i+1:],stop,lev+1)
        for j in range(len(L)):
            L[j] += c
        toRet += L
    return toRet
def circ(s):
    L = []
    for i in range(len(s)):
        L.append(s[i:]+s[:i])
    return L
def prim_right_tri(P):
    sol = []
    n = P//2
    a = int((n/2)**0.5)
    b = int(n**0.5)
    for x in range(a,b+1):
        for y in range(1,x):
            if gcd(x,y)==1 and x*(x+y)==n:
                sol.append(sorted([2*x*y , x**2 - y**2 , x**2 + y**2]))
    return sol
def factors(n):
    D = PF(n)
    L = [1]
    for p in D:
        Ln = []
        for i in range(1,D[p]+1):
            for l in L:
                Ln.append(l*(p**i))
        L = Ln + L
    return L 
def right_tri(P):
    sol = []
    for f in factors(P):
        ns = prim_right_tri(P//f)
        for s in ns:
            for i in range(len(s)):
                s[i] *= f
            if s not in sol:
                sol.append(s)

    return sol
def isPent(x):
    n = (1 + (1 + 24*x)**0.5)/6
    if n == int(n):
        return True
