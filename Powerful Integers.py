class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ans = set()
        i = 0
        j = 0
        while x**i + y**j <= bound:
            while x**i + y**j <= bound:
                ans.add(x**i+y**j)
                j+=1
                if y < 2:
                    break
            j=0
            i+=1
            if x < 2:
                break
        return list(ans)

solution = Solution()
# print(solution.powerfulIntegers(2,3,10) == [2,3,4,5,7,9,10])
# print(solution.powerfulIntegers(3,5,15) == [2,4,6,8,10,14])
print(solution.powerfulIntegers(1,2,100))