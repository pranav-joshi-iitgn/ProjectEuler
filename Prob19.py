d = [1,4,4,0,2,5,0,3,6,1,4,6]
s = 0
year = 1900
leap = False
def update():
    global leap,year,d
    if(leap):
        d[0] = (d[0]+2)%7
        d[1] = (d[1]+2)%7
    else:
        d[0] = (d[0]+1)%7
        d[1] = (d[1]+1)%7
    year += 1
    if(year%4!=0 or ((year%100==0) and (year%400!=0))):
        leap = False
        for i in range(2,12):
            d[i] = (d[i]+1)%7
    else:
        leap = True
        for i in range(2,12):
            d[i] = (d[i]+2)%7
for y in range(100):
    update()
    for md in d:
        if(md==0):
            s += 1
print(s,year)
