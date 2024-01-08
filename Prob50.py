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
N = 10**6
P,iP = generatePrimes(N-1)

S = 0
for i in range(len(P)):
    S += P[i]
    if S >= N:
        L = i
        break


con = True
for l in range(L+10,0,-1):
    if not con:
        break
    S = 0
    for i in range(l):
        S += P[i]
    while S < N:
        if iP[S]:
            print(S)
            con = False
            break
        i += 1
        S += P[i] - P[i-l]
