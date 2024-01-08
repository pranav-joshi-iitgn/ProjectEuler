from math import gcd
def prT(P):
    sol = []
    n = P//2
    a = int((n/2)**0.5)
    b = int(n**0.5)
    for x in range(a,b+1):
        for y in range(1,x):
            if gcd(x,y)==1 and (x-y)%2==1 and x*(x+y)==n:
                sol.append(sorted([2*x*y , x**2 - y**2 , x**2 + y**2]))
    return sol


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
 

def tr(P):
    sol = []
    for f in factors(P):
        ns = prT(P//f)
        for s in ns:
            for i in range(len(s)):
                s[i] *= f
            if s not in sol:
                sol.append(s)

    return sol

m = 0
j = 0
for i in range(1,10000):
    if len(prT(i)) > m:
        m = len(prT(i))
        j= i

print(j,prT(j))