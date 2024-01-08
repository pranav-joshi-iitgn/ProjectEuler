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

N = 2000

P = generatePrimes(N)
Q = generatePrimes(2*N)

def isPrime(n):
    if(n==2):
        return True
    if(n%2==0):
        return False
    d = 3
    m = int(n**0.5)
    while d <= m :
        if(n%d == 0):
            return False
        d += 2
    return True

def SeqLen(a,b):
    f = b
    n = 0
    while True:
        if (f<0) or (not isPrime(f)):
            return n
        f += a + 2*n + 1
        n += 1
    
maxlen = 0
for p in P:
    for q in Q:
        a = q-p-1
        check = p%q
        F = check**2 + a*check + p
        if(check<maxlen and F!=q):
            continue
        check = (q-1)%p
        F = check**2 + a*check + p
        if(check<maxlen and F!=p):
            continue
        curlen = SeqLen(a,p)
        if curlen > maxlen:
            maxlen = curlen
            print(a,p,curlen)  