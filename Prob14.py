from numpy import argmax
Lengths = {1:0,2:1,4:2,8:3}
N = 1000000
ImpLengths = {}
def rCJ(n,l):
    if n < N :
        ImpLengths[n] = Lengths[n]
    if l == 0:
        return
    if n%3 != 0:
        Lengths[2*n] = Lengths[n] + 1
        rCJ(2*n,l-1)
        if n%2 == 0 and n%3 == 1:
            Lengths[(n-1)//3] = Lengths[n] + 1
            rCJ((n-1)//3,l-1)

def C(n):
    if n%2 == 0:
        return n//2
    return 3*n + 1

L = [0]*(N+1)
L[2] = 1
for n in range(2,N+1):
    S = []
    x = 0
    while x==0:
        S.append(n)
        n = C(n)
        if n <= N :
            x = L[n]
    l0 = L[n]
    S_len = len(S)
    for l in range(1,S_len+1):
        x = S[S_len - l]
        if x <= N :
            L[x] = l0 + l
print(argmax(L))