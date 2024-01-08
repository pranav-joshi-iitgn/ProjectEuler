a = range(1,30000)
b = [0]*30000
for i in a:
    j = 2*i
    while j<30000:
        b[j] += i
        j += i
S = 0
for i in range(1,10000):
    if b[i]!=i and b[b[i]]==i: 
        S += i
print(S)
