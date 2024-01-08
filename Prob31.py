def makes(N,L):
    if len(L)==1 :
        if N%L[0] == 0:
            return 1
        else:
            return 0
    d = L[0]
    L = L[1:]
    S = 0
    while N >= 0 :
        S += makes(N,L)
        N -= d
    return S

print(makes(200,[200,100,50,20,10,5,2,1]))