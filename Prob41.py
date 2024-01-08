def perm(s):
    if len(s) == 1:
        return [s]
    P = []
    for i in range(len(s)) :
        p = perm(s[:i]+s[i+1:])
        for j in range(len(p)):
            p[j] = s[i] + p[j]
        P += p
    return P

def isPrime(x):
    if x<=1:
        return False
    if x==2:
        return True
    if x%2 == 0:
        return False
    m = int(x**0.5)
    for i in range(3,m+2):
        if x%i == 0:
            return False
    return True


P = perm('7654321')
for p in P:
    if isPrime(int(p)):
        print(p)
        break