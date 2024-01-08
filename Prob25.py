from math import log10,sqrt
phi = ((sqrt(5))+1)/2
d = 1000
c = 1
x = 1
y = 1
while x < 10**(d-1):
    z = x + y
    x = y
    y = z
    c += 1
print(c,(d-1+log10(5)/2)/log10(phi))
