class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for y in range(2, len(grid)):
            for x in range(2, len(grid[y])):
                sum = grid[y][x-2] + grid[y][x-1] + grid[y][x]
                if self.numbersBetween1To9(grid, x, y) \
                        and sum == grid[y-2][x-1] + grid[y-1][x-1] + grid[y][x-1] \
                        and sum == grid[y-2][x-2] + grid[y-1][x-2] + grid[y][x-2] \
                        and sum == grid[y][x-2] + grid[y][x-1] + grid[y][x] \
                        and sum == grid[y-1][x-2] + grid[y-1][x-1] + grid[y-1][x] \
                        and sum == grid[y-2][x-2] + grid[y-2][x-1] + grid[y-2][x] \
                        and sum == grid[y][x] + grid[y-1][x-1] + grid[y-2][x-2] \
                        and sum == grid[y-2][x] + grid[y-1][x-1] + grid[y][x-2]:
                    result += 1

        return result

    def numbersBetween1To9(self, grid, x, y):
        for i in range(y-2,y+1):
            for j in range(x-2,x+1):
                if grid[i][j] > 9 or grid[i][j] < 1:
                    return False
        return True

solution = Solution()
print(solution.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
print(solution.numMagicSquaresInside([[7,0,5],[2,4,6],[3,8,1]]))
print(solution.numMagicSquaresInside([[10,3,5],[1,6,11],[7,9,2]]))
print(solution.numMagicSquaresInside([[7,6,2,2,4],[4,4,9,2,10],[9,7,8,3,10],[8,1,9,7,5],[7,10,4,11,6]]))