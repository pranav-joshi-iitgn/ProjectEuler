from math import factorial

def incSeq(low,high,size):
    if high < low :
        return []
    if size <= 0:
        return []
    if size==1:
        return list(map(str,range(low,high+1)))
    L = []
    for i in range(low,high+1):
        l = incSeq(i,high,size-1)
        for j in range(len(l)):
            l[j] = str(i) + l[j]
        L += l
    return L

occ = []
for size in range(1,6):
    L = incSeq(0,9,size)
    for x in L:
        s = 0
        for d in x:
            s += factorial(int(d))
        if x == "".join(sorted(str(s))) and s not in occ:
            occ.append(s)

print(occ)