def muxer(l):
    r=[]
    x=len(l[0])
    for i in range(x):
        for elemento in l:
            r.append(elemento[i])
    return r

print(muxer([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]))

