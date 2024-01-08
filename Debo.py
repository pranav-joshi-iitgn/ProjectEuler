def checkprime(a):
    b=0
    for i in range(1,a+1):
        if a%i==0:
            b=b+1
    if b==2:
        return True
    else:
        return False
    

factors=[]
a=int(input("Enter a number : "))
if a==1 or a==0 or a<0:
    print(a, "is not a prime number")
else:
    for i in range (2,a):
        if a%i==0:
            if checkprime(i) is True:
                factors.append(i)

print("The factors of the number ",a,"are", factors)