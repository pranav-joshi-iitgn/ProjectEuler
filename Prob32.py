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

P = perm('123456789',5)

occ = 0
S = 0
C = []


for i in [1,2]:
    for p in P:
        a = p[:i]
        b = p[i:]
        c = str(int(a) * int(b))
        full = a+b+c
        if "".join(sorted(full)) == "123456789" and c not in C:
            occ += 1
            C.append(c)
            print(a,b,c)
            S += int(c)

print(occ,S)