S = 0
for a in range(1,100):
    for b in range(1,100):
        s = sum(map(int,str(a**b)))
        if s > S:
            S = s

print(S)