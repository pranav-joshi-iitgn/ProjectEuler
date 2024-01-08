def isPent(x):
    n = (1 + (1 + 24*x)**0.5)/6
    if n == int(n):
        return True
    
p = 1
D = 10**10
while 3*p-2 <= D:
    A = p*(3*p-1)//2
    for q in range(1,p):
        B = q*(3*q-1)//2
        C = A-B
        if isPent(C) and isPent(A+B):
            print(C,B,A,A+B)
            if C < D:
                D = C
    p += 1

