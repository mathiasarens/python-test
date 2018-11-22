# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = [0 for i in range(len(arr)+1)]
    dp[0] = 0
    maximum_sum = -2**31
    for i in range(1,len(dp)):
        if i > 1:
            maximum_sum = max(maximum_sum, dp[i-2])
            maximum_sum = max(maximum_sum, dp[i-2] + arr[i-1])
        maximum_sum = max(maximum_sum, arr[i-1])
        dp[i] = maximum_sum

    return dp[len(dp)-1]

print(maxSubsetSum([-2,1,3,-4,5])==8)
print(maxSubsetSum([3,7,4,6,5])==13)
print(maxSubsetSum([2,1,5,8,4])==11)
print(maxSubsetSum([3,5,-7,8,10])==15)