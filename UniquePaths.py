class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        matrix = [[ 1 for i in range(n) ] for j in range(m)]
        i,j = 0,0
        while i < m:
            j = 0
            while j < n:
                if i == 0 and j > 0:
                    matrix[i][j] = 1
                if j == 0 and i > 0:
                    matrix[i][j] = 1
                if i > 0 and j > 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                j+=1
            i+=1
        return matrix[m-1][n-1]

solution = Solution()
# print(solution.uniquePaths(0,0))
#print(solution.uniquePaths(1,0))
print(solution.uniquePaths(1,1))
# print(solution.uniquePaths(2,1))
# print(solution.uniquePaths(1,2))
# print(solution.uniquePaths(3,2))
print(solution.uniquePaths(7,3))