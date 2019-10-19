##funzione ricorsiva
def soldi(x,r,n):
    if(n==0):
        return x
    elif(n>0):
        return soldi(x+r*x,r,n-1)
##funzione matematica
"""
import math
def soldi(x,r,n):
    if(n==0):
        return x
    elif(n>0):
        return x*pow(1+r,n)
"""
print(soldi(input("x?\n"),input("r?\n"),input("n?\n")))


