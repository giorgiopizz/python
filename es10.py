import math
#la lista contiene 32 elementi
def mergesort(list):
    for j in range(1,int(math.log(len(list),2))+1):
        for i in range(len(list)//(pow(2,j))):
            #ordino la lista i-esima con 2^j elementi sapendo che e composta da due liste ordinate con
            #2^(j-1) elementi
            a=0
            b=0
            k=pow(2,j)*i
            lefthalf=list[pow(2,j)*i:pow(2,j)*i+pow(2,j-1)]
            righthalf=list[pow(2,j)*i+pow(2,j-1):pow(2,j)*i+pow(2,j)]
            while(a<pow(2,j-1)) and (b<pow(2,j-1)):
                if(lefthalf[a]>righthalf[b]):
                    list[k]=righthalf[b]
                    k=k+1
                    b=b+1
                else:
                    list[k]=lefthalf[a]
                    a=a+1
                    k=k+1
            while(a<pow(2,j-1)):
                list[k]=lefthalf[a]
                k=k+1
                a=a+1
            while(b<pow(2,j-1)):
                list[k]=righthalf[b]
                k=k+1
                b=b+1
    print(list)

mergesort([8,2,1,4,6,9,11,17,32,5,15,23,8,13,3,19])





