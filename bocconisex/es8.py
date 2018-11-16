def fibperiod(k):
    i=0
    x=0
    y=1
    #z e l'indice di fine periodo
    z=0
    while(i!=-1):
        w=x+y
        x=y
        y=w
        if (x%k==0 and y%k==1):
            z=i
            i=-1
        else:
            i=i+1
    return(z+1)

print(fibperiod(input("k?")))

