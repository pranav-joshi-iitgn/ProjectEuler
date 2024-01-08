P = [2,3,5,7,11,13,17]
def ext(s,n=0):
    global P
    R = []
    L = list(range(10))
    for c in s :
        L.remove(int(c))
    if len(L)==0:
        return [s]
    x = int(s[-2:])*10
    for d in L:
        if (x+d)%P[n] == 0:
            r = ext(s + str(d),n+1)
            R += r
    return R


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

I = []

for d in range(1,10):
    L = list(range(10))
    L.remove(d)
    s = ''
    for c in L:
        s += str(c)
    L = perm(s,2)
    for i in range(len(L)):
        L[i] = str(d) + L[i]
    I += L
    


L = []

for i in I:
    L += ext(i)


S = 0
for l in L:
    S += int(l)

print(S)