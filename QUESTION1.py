def paircount(l1, n, sum):
    count = 0  
    for i in range(0,n):
        for j in range(i+1,n):
            if l1[i]+l1[j] == sum:
                count += 1
    return count
l1 = [2,7,4,1,3,6]
n = len(l1)
sum = 10
print("total no of pairs is  ",paircount(l1, n, sum))
