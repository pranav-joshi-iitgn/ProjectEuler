L = [[0]]
R = -1
c = 0
for n in range(1,101):
    lo = L[-1]
    l = []
    l.append(1)
    if R==-1:
        N = n
    else:
        N = R
    for r in range(1,N):
        x = lo[r-1]+lo[r]
        if x > 10**6:
            R = r
            break
        l.append(x)
    if R == -1:
        l.append(1)
        c += n+1
    else:
        c += 2*R
    L.append(l)
    print(l)

print(5150 -c)


