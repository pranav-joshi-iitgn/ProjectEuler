N = 10**6
L = [True]*(N+1)
L[0] = False
L[1] = False
for i in range(2,N+1):
    if(L[i]):
        j = 2*i
        while j <= N :
            L[j] = False
            j += i

can = L.copy()

for i in range(2,N,2):
    can[i] = True

for i in range(2,N+1):
    if not can[i]:
        print(i)
        break
    if(L[i]):
        j = 1
        x = i + 2
        while x <= N :
            can[x] = True
            j += 1
            x = i + 2*(j**2)
    