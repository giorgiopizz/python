import sys
def drawtri(n):
    for i in range(0,n+2,1):
        if(i==0):
            sys.stdout.write("o\n")
        elif(i==n+1):
            sys.stdout.write("o")
            for j in range(0,n,1):
                sys.stdout.write("-")
            sys.stdout.write("o\n")
        else:
            sys.stdout.write("|")
            for j in range(0,i-1,1):
                sys.stdout.write(" ")
            sys.stdout.write("\\")
            sys.stdout.write("\n")

drawtri(input("Lunghezza lati?"))

