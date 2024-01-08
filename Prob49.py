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
    return primes,L
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


P,iP = generatePrimes(10**4-1)
A = []
for p in P:
    ps = str(p)
    L = perm(ps,len(ps))
    Ln = []
    for l in L:
        if l != ps:
            Ln.append(l)
    L = Ln
    for ps2 in L:
        p2 = int(ps2)
        p1 = p + p2
        if p1%2==1:
            continue
        p1 = p1//2
        if str(p1) not in L:
            continue
        if not (iP[p] and iP[p1] and iP[p2]):
            continue
        m = min(L+[ps])
        if m not in A:
            A.append(m)
            print([p,p1,p2])




