def maxDifference(a):
    maximum_value = -1
    minimum_value = a[0]
    for i in range(1,len(a)):
        maximum_value = max(maximum_value,a[i]-minimum_value)
        minimum_value = min(minimum_value, a[i])
    return maximum_value

print(maxDifference([1,2,6,4])==5)
print(maxDifference([4,3,2,1])==-1)
print(maxDifference([1])==-1)