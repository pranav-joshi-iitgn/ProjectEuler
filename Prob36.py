S = 0
for i in range(10**6):
    d = str(i)
    b = bin(i)
    if (b[2:len(b)//2+1]==b[:len(b)-len(b)//2:-1]) and (d[:len(d)//2]==d[:len(d)-len(d)//2 -1:-1]):
        S += i

print(S)