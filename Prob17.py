Ones = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]
#Ones = [len(x) for x in Ones]
First2Ds = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]
Tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]
def Word(n):
    o = n%10
    n = n//10
    t = n%10
    n = n//10
    h = n%10
    n = n//10
    th = n%10

    if t == 0:
        s = Ones[o]
    elif t == 1:
        s = First2Ds[o]
    else:
        s = Tens[t] + " " + Ones[o]
    
    if h > 0 :
        if s == "":
            s = Ones[h] + " hundred"
        else :
            s = Ones[h] + " hundred and " + s

    if th > 0 :
        s = Ones[th] + " thousand " + s
    
    return s

def Length(w):
    l = 0
    for c in w :
        if c != " ":
            l += 1
    return l

S = 0
for i in range(1001):
    S += Length(Word(i))

print(S)