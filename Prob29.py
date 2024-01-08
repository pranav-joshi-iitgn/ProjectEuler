from math import lcm
L = [True]*101
L[0] = False
L[1] = False
def mul(l,m):
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

def all(L):
    if len(L) == 1:
        return 99
    if len(L) == 0:
        return 0
    m = lcm(L[0],L[1])
    for i in range(2,len(L)):
        m = lcm(m,L[i])
    a = min(L)
    b = a*100
    return mul([a,b],m) 

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

S = 0
for a in range(2,101):
    if L[a]:
        x = a
        b = 0
        while x < 101:
            L[x] = False
            x = x * a
            b += 1
        S += one(b)

print(S)