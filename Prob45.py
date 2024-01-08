def isPent(x):
    n = (1 + (1 + 24*x)**0.5)/6
    if n == int(n):
        return True

n = 144
while True:
    H = n*(2*n-1)
    if isPent(H):
        print(H)
        break
    n += 1