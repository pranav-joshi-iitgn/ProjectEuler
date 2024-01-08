from math import factorial
s = ""
N = 999999
L = []
d = 10
for i in range(d):
    s = s + str(N//factorial(d-1-i))
    N = N%factorial(d-1-i)
    L.append(str(i))
print(s)
S = ""
for i in s:
    S += L[int(i)]
    L.pop(int(i))
print(S)