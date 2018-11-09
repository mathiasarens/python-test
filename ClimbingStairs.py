class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0]*(max(n,2)+1)
        result[1] = 1
        result[2] = 2
        for i in range(3,n+1):
            result[i] = result[i-2]+result[i-1]
        return result[n]

solution = Solution()
print(solution.climbStairs(6))

# 111111
# 1212
# 1122
# 1221
# 2112
# 2211
# 222