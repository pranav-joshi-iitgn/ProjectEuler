P = [True]*(10**6)
P[0] = P[1] = False
C = [False]*(10**6)
for i in [2,3,5,7]:
    C[i] = True

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

for p in range(10**6):
    if P[p]:
        x = p*2
        while x < 10**6:
            P[x]=False
            x += p

for p in range(10**6):
    if P[p]:
        if C[p]:
            continue
        c = True
        ps = str(p)
        for bad in ['0','2','4','6','8','5']:
            if bad in ps:
                c = False
                break
        if not c:
            continue
        ps = circ(ps)
        for x in ps:
            if not P[int(x)]:
                c = False
                break
        if c :
            for x in ps:
                C[int(x)] = True

circ = []
for c in range(2,10**6):
    if C[c]:
        circ.append(c)

print(circ,len(circ))



