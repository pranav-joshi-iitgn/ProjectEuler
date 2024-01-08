n = 6
N = 10**n
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

def grow(s):
    L = ['']
    for c in s :
        if c == '*':
            l = len(L)
            for i in range(l):
                L[i] += '*'
        if c == '_':
            l = len(L)
            for d in map(str,range(1,10)):
                for i in range(l):
                    L.append(L[i]+d)
            for i in range(l):
                L[i] += '0'
    return L

def fam(s):
    F = []
    if '*' not in s :
        return [s]
    for d in map(str,range(1,10)):
        x = int(s.replace('*',d))
        if L[x]:
            F.append(x)
    good = True
    for c in s :
        if c == '0':
            continue
        elif c == '*':
            good = False
            break
        else:
            break
    if good:
        x = int(s.replace('*','0'))
        if L[x]:
            F.append(x)
    return F

def convto11(x):
    s = ''
    while x != 0:
        r = x % 11
        if r == 10 :
            r = '*'
        else :
            r = str(r)
        s = r + s
        x = x // 11
    return s

def convfrom11(s):
    x = 0
    b = 1
    for c in s[::-1]:
        if c == '*':
            x += 10 * b
        else:
            x += int(c) * b
        b *= 11
    return x

def generateFam(x):
    L = [str(x)]
    l = len(str(x))
    for j in range(l-1):
        n = len(L)
        for i in range(n):
            s = L[i]
            s = s[:j] + '*' + s[j+1:]
            L.append(s)
    return L

F = [0]*(11**n)
P = [0]*(11**n)

for p in primes :
    for s in generateFam(p):
        x = convfrom11(s)
        if P[x] == 0:
            P[x] = p
        if F[x] == 6 :
            print(s)
            break
        F[convfrom11(s)] += 1

print(generateFam(12367))
#F = [conv(x) for x in range(1,10**(n-1))]


#print(len(F))