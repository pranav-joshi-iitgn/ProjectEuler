L = sorted(open("Prob22.txt").read().split(","))
S = 0
for i in range(len(L)):
    n = 0
    for j in range(1,len(L[i])-1):
        n += ord(L[i][j]) - 64
    S += n*(i+1)
print(S)
