from math import comb
def F(n):
    i = 0
    j = 1
    x = 0
    while(j <= n):
        x += comb(n,j) * 5**(i)
        i += 1
        j = 2*i + 1
    x /= 2**(n-1)
    return int(x)
r = 1
f = F(3)
S = 0
while(f<=4000000):
    S += f
    r+=1
    f = F(3*r)
print(S)
print(r)
print(f)