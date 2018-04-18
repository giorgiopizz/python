def interestdays(x, y, r):
    i=1
    sum=x
    while(i!=-1):
        sum=sum+sum*r/100
        if(sum>=y):
            return i
            i=-1
        else:
            i=i+1
print(interestdays(input("x?\n"),input("y?\n"),input("r?")))

