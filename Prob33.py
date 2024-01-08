from fractions import Fraction
from math import prod
F = Fraction(1,1)
for b in range(10,100):
    for a in range(10,b):
        triv = False
        can = False
        f = Fraction(a,b)
        a1 = list(str(a))
        b1 = list(str(b))
        for d in str(a):
            if d == '0':
                triv = True
            if d in b1:
                a1.remove(d)
                b1.remove(d)
                can = True
        if triv:
            continue
        a1 = ''.join(a1)
        b1 = ''.join(b1)
        if not len(a1):
            a1 = 1
            b1 = 1
        else:
            a1 = int(a1)
            b1 = int(b1)

        if b1 == 0:
            continue

        f1 = Fraction(a1,b1)
        if f == f1 and can:
            print(a,b)
            F = F*f

print(F)