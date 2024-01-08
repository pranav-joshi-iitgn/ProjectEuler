S = 0
for i in range(2,10**6):
    x = i
    s = 0
    while x > 0 :
        s += (x % 10)**5
        if s > i :
            break
        x = x//10
    if s == i:
        S += s
print(S)

"""
d*(9**5) > s = i >= 10**(d-1) 
for any number i that satisfies the criterion. 'd' is number of digits in i.
Thus, d*(9**5) >  10**(d-1)
This inequality is false fall all d > 6
So i can be a 6 digit number at most. Thus i < 10**6
"""