L = open("Project_Euler/grid.txt").read().split('\n')
M = [list(map(int,r.split())) for r in L]

def rows(M):
    return M
def collumns(M):
    L = []
    m = len(M)
    n = len(M[0])
    for j in range(n):
        C = [M[i][j] for i in range(m)]
        L.append(C)
    return L
def upDiagonals(M):
    L = []
    m = len(M)
    n = len(M[0])
    for k in range(m+n-1):
        C = [M[i][k-i] for i in range(max(k-n+1,0),min(k+1,m))]
        L.append(C)
    return L
def downDiagonals(M):
    L = []
    m = len(M)
    n = len(M[0])
    for k in range(1-n,m):
        C = [M[i][i-k] for i in range(max(k,0),min(k+n,m))]
        L.append(C)
    return L
def Split(L):
    newL = []
    l = []
    for x in L:
        if x ==0 :
            if len(l) != 0:
                newL.append(l)
                l = []
        else:
            l.append(x)
    if len(l)!= 0:
        newL.append(l)
    return newL

def maxP(L):
    if len(L)<4 :
        return 0
    x = 1
    for i in range(4):
        x *= L[i]
    f = x
    for i in range(len(L)-4):
        x = x//L[i]
        x *= L[i+4]
        if x > f :
            f = x
    return f
    
def MAXP(L):
    m = 0
    for l in L:
        m = max(m,maxP(l))
    return m

def max_from_rows(M):
    m = 0
    for r in M :
        m = max(m,MAXP(Split(r)))
    return m 

def max_from_collumns(M):
    m = 0
    for c in collumns(M) :
        m = max(m,MAXP(Split(c)))
    return m 

def max_from_up_diagonals(M):
    m = 0
    for D in upDiagonals(M) :
        m = max(m,MAXP(Split(D)))
    return m 

def max_from_down_diagonals(M):
    m = 0
    for D in downDiagonals(M) :
        m = max(m,MAXP(Split(D)))
    return m 

X = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
L = [
    max_from_rows(M),
    max_from_collumns(M),
    max_from_down_diagonals(M),
    max_from_up_diagonals(M)
]
Max = 0 
for i in L:
    Max = max(Max,i)
print(Max)
