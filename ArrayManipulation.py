def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for (p, q, sum) in queries:
        arr[p]+=sum
        if (q+1<=n): 
            arr[q+1]-=sum
    max_value = 0
    sum = 0
    for i in range(1,len(arr)):
        sum += arr[i]
        max_value = max(max_value, sum)
    return max_value


print(arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]])==10)
print(arrayManipulation(5, [[1,2,100], [2,5,100], [3,4,100]])==200)