S = open("Prob13.txt",'r').read().split()
n = 0
k = 13
for x in S :
    n += int(x[:13])
while n%1000 >= 900:
    n = 10*n
    for x in S:
        n += int(x[k])
    k += 1
print(str(n)[:10])


