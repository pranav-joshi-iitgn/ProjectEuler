def t(n):
    return (n*(n+1))//2

def PF(n):
    D = {}
    x = 2
    while n != 1:
        if n%x == 0:
            if x in D :
                D[x] += 1
            else :
                D[x] = 1
            n = n//x
        else :
            if x*x > n :
                D[n] = 1
                break
            x += 1
    return D
    
def DoT(n):
    D1 = PF(n)
    D2 = PF(n+1)
    for x  in D2 :
        if x in D1:
            D1[x] += D2[x]
        else:
            D1[x] = D2[x]
    D1[2] += -1
    NoD = 1
    for x in D1:
         NoD *= D1[x] + 1
    return NoD

x = 1
N = 500
while DoT(x) <= N:
    x += 1

print(t(x))
        