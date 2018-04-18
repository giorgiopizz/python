def revert(list):
    m=len(list)//2
    for i in range(m):
        x=list[i]
        y=list[len(list)-1-i]
        list[i]=y
        list[len(list)-1-i]=x
    return list
print(revert([0,54,92,2,6,8]))



