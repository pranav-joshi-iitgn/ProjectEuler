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

def isLT(x):
    s = str(x)
    for i in range(len(s)):
        x = int(s[i:])
        if not isPrime(x):
            return False
    return True

R = [[2,3,5,7]]
c = 0
while True:
    newR = []
    for d in [1,3,7,9]:
        for r in R[-1]:
            newr = int(str(r)+str(d))
            if isPrime(newr):
                newR.append(newr)
                c += 1
    if len(newR) == 0:
        break
    R.append(newR)

T = []

for r in R:
    for x in r :
        if isLT(x):
            T.append(x)
T = T[4:]

print(T,len(T),sum(T))

