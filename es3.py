
##The Collatz conjecture

i=0
def collatz(m):
    i=i+1
    if(m==1):
        return(i)
    else:
        if m%2==0:
            return(collatz((m//2)))
        
        else:
            return(collatz((m*3)+1))

print(collatz(12))

