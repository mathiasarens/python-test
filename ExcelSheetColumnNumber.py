class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            ans += (ord(s[i])-ord('A')+1)*pow(26, len(s)-i-1)
        return ans

solution = Solution()
print(solution.titleToNumber("A") == 1)
print(solution.titleToNumber("B") == 2)
print(solution.titleToNumber("C") == 3)
print(solution.titleToNumber("Z") == 26)
print(solution.titleToNumber("AA") == 27)
print(solution.titleToNumber("AB") == 28)
print(solution.titleToNumber("ZY") == 701)
            
