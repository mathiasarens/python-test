class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self._binarySearch(x, 0, x)
        
    def _binarySearch(self, target, lower, upper):
        if upper-lower <1:
            return upper
        if upper-lower < 2:
            if upper*upper == target:
                return upper
            else:
                return lower
        middle = lower + (upper-lower)//2
        if middle*middle>target:
            return self._binarySearch(target, lower, middle)
        else:
            return self._binarySearch(target, middle, upper)

solution = Solution()
print(solution.mySqrt(0) == 0)
print(solution.mySqrt(1) == 1)
print(solution.mySqrt(2) == 1)
print(solution.mySqrt(3) == 1)
print(solution.mySqrt(4) == 2)
print(solution.mySqrt(5) == 2)
print(solution.mySqrt(8) == 2)
print(solution.mySqrt(9) == 3)
print(solution.mySqrt(10) == 3)
print(solution.mySqrt(9))