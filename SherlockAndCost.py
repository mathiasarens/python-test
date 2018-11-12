def cost(B):
    dp = [[0 for i in range(2)] for i in range(len(B))]

    for i in range(len(B)-1):
        dp[i+1][0] = max(dp[i][0], dp[i][1]+abs(B[i]-1))  # 1
        dp[i+1][1] = max(dp[i][0] + abs(1-B[i+1]), dp[i]
                         [1] + abs(B[i]-B[i+1]))  # max

    return max(dp[len(B)-1][0], dp[len(B)-1][1])


print(cost([1, 2, 3]) == 2)
print(cost([1, 1, 4, 1, 1, 2]) == 7)
print(cost([10, 1, 10, 1, 10]) == 36)
print(cost([100, 2, 100, 2, 100]) == 396)

# 3 2 3
# 3 1 3
#   2 2
# 1 2 3
#   1 1

# vorher:
# 1
# max

# hit a number
# 1    max
# max   1

# 1 1 4 1 1 2
#  0 3 3 0 1 = 7
# 100 2 100 2 100
# 100 1 100 1 100
#    99 -9999 -99

# 3 4 5 6 7 1 6
# 1 4 1 6 1 1 6
#   3 3 5 5 0 6

# 3 1 5 1 7 1 6
#   2 4 4 6 6 5

#
