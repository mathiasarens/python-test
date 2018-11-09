class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        if dividend > 2**31-1 or dividend < -2**31 or divisor > 2**31-1 or divisor < -2**31:
            return 2**31-1
        current_dividend = abs(dividend)
        current_divisor = abs(divisor)
        quotient = 0
        temp = 0
  
        # test down from the highest bit and 
        # accumulate the tentative value for 
        # valid bit 
        for i in range(31, -1,-1):
            if temp + (current_divisor << i) <= current_dividend:
                temp += current_divisor << i
                quotient += 1 << i
            
        if (dividend < 0) ^ (divisor < 0):
            return quotient * -1
        else:
            return quotient

solution = Solution()
print(solution.divide(10,2) == 5)
print(solution.divide(9,2) == 4)
print(solution.divide(9,-2) == -4)
print(solution.divide(9,-22) == 0)
print(solution.divide(1,1) == 1)
print(solution.divide(-1,1) == -1)
print(solution.divide(1,-1) == -1)
print(solution.divide(-1,-1) == 1)
print(solution.divide(-2**31+1,-1) == 2147483647)
print(solution.divide(-2**31+1,-2) == 1073741823)
print(solution.divide(-2147483648,-1) == 2147483647)
print(solution.divide(-2147483648,1) == -2147483648)
print(solution.divide(-2147483648,2) == -1073741824)

