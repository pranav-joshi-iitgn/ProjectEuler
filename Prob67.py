S = open("Prob67.txt",'r').readlines()
S = [[0] + list(map(int,s[:-1].split())) + [0] for s in S]
S = [[0,0]] + S
for i in range(1,len(S)):
    for j in range(1,i+1):
        S[i][j] += max(S[i-1][j-1],S[i-1][j])
print(max(S[-1]))
