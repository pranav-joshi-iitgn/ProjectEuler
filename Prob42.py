L = open('Prob42.txt').read().split('","')
L[0] = L[0][1:]
L[-1] = L[-1][:-1]

s ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
D = {}
v = 1
for c in s:
    D[c] = v
    v += 1

for i in range(len(L)):
    V = 0
    for c in L[i]:
        V += D[c]
    L[i] = V

T = [n*(n+1)//2 for n in range(1,21)]

occ = 0

for v in L :
    if v in T:
        occ += 1

print(occ)