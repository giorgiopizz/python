from __future__ import division
def fibonacci(n):
   i=1
   #x e l'ennesimo termine della successione e y l'ennesimo piu uno
   x=1
   y=1
   while(i!=n):
        z=x+y
        x=y
        y=z
        i=i+1
   return y/x

      
print(fibonacci(100))



