'''
10 = 2*5 
9 = 1*9 = 3*3 = 9*1
'''

def parts(s):
    P = []
    p = []
    l = len(s)
    p.append(int(s[0]))
    for i in range(1,5):
        x = int(s[2*i-1]+s[2*i])
        p.append(x)
    P.append(p)
    p = []
    p.append(int(s[:4]))
    p.append(int(s[4:]))
    P.append(p)
    for i in [1,3]:
        p = []
        for j in range(9//i):
            p.append(int(s[i*j:(j+1)*i]))
        P.append(p)
    return P

def check(N):
    P = parts(str(N))
    for p in P:
        n = len(p)
        good = True
        for i in range(1,n):
            if p[i] != (i+1)*p[0]:
                good = False
                break
        if good:
            print(p)
            return True
    return False

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

P = perm('987654321')

for p in P:
    if check(p):
        print(p)
        break

        


    