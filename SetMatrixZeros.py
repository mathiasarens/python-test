class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_0_is_null = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                row_0_is_null = True
            for column in range(1,len(matrix[row])):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0
        for row in range(1,len(matrix)):
            for column in range(1,len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0
        if matrix[0][0] == 0:
            for column in range(1,len(matrix[0])):
                matrix[0][column]=0
        if row_0_is_null:
            for row in range(len(matrix)):
                matrix[row][0] = 0




solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))