S = open("Project_Euler/Number.txt").read()
S = "".join(S.split('\n'))
L = S.split('0')
f = 0
for S in L :
    if len(S)<13:
        continue
    x = 1
    for i in range(13):
        x *= int(S[i])
    if x>f :
        f = x
    for i in range(len(S)-13):
        x = x // int(S[i])
        x *= int(S[i+13])
        if x > f :
            f = x
print(f)
    

