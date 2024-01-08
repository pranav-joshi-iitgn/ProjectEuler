from math import gcd
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

def Ab(n):
    L = [1]*(n+1)
    A = []
    for i in range(2,n):
        j = 2*i
        while j <= n :
            L[j] += i
            j += i
    for i in range(1,n):
        if L[i] > i :
            A.append(i)
    return A

def PrimA(n):
    L = [1]*(n+1)
    P = []
    for i in range(2,n):
        j = 2*i
        while j <= n :
            L[j] += i
            j += i
    L[0] = False
    for i in range(1,n):
        if L[i] == False:
            continue
        if L[i] > i :
            L[i] = True
            P.append(i)
            j = 2*i
            while j <= n:
                L[j] = False
                j += i
        else:
            L[i] = False
    return P

# This function is of more than n**2 complexity somehow
def SoAn(n):
    c = 0
    G = []
    P = PrimA(n)
    L = [False]*(n+1)
    F = []
    for a in range(len(P)):
        p = P[a]
        for b in range(a,len(P)):
            q = P[b]
            x = p*q
            g = gcd(p,q)
            for i in range(1,q):
                for j in range(1,p):
                    y = p*i + q*j
                    if(y > n or y > x):
                        break
                    L[y] = True
            for g2 in G :
                if g%g2==0:
                    continue
            while x <= n :
                L[x] = True
                x += g
                c += 1
            G.append(g)
    for i in range(1,n+1):
        if L[i]:
            F.append(i)
    print(c)
    return F

def SnSoA(n):
    A = Ab(n)
    L = [False]*(n+1)
    S = 0
    for a in range(len(A)):
        p = A[a]
        for b in range(a,len(A)):
            q = A[b]
            if(p+q<=n):
                L[p+q] = True
            else:
                break
    for i in range(1,n+1):
        if not L[i]:
            S += i
    return S
    
    
N = 28123
print(SnSoA(N))
