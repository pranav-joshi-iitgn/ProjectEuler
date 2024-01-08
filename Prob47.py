N = 10**6
L = [0]*N
for i in range(2,N):
    if L[i]==0:
        for j in range(i,N,i):
            L[j] += 1

for i in range(2,N):
    good = True
    for j in range(i,i+4):
        if L[j] != 4:
            good = False
            break
    if good:
        print(i)
        break
