class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        result = self.myPow(x, n//2)
        if n%2==0:
            return result * result
        if n > 0:
            return result * result * x
        else:
            return result * result / x
    
solution = Solution()
print(solution.myPow(2.1,3)==9.26100)
print(solution.myPow(2,10)==1024)