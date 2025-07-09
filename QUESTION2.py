def minmaxrange(l2,n):
    max = l2[0]
    min = l2[0]
    for i in range(1,n):
         if max<l2[i] :
             max =l2[i]
    for j in range (1,n):
        if min > l2[j] :
            min =l2[j]
    return (max,min) 
#l2 = list(int(input()))    
l2 = [5,3,8,1,0,4]
n = len(l2)
#print (l1)
print ("the range is",minmaxrange(l2,n))
