import sys


class Solution:

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value1 = sys.maxsize
        value2 = sys.maxsize
        for i in range(len(nums)):
            if nums[i] <= value1:
                value1 = nums[i]
            elif nums[i] <= value2:
                value2 = nums[i]
            else:
                return True
        return False


solution = Solution()
# print(solution.increasingTriplet([1,2,3,4,5]))
# print(solution.increasingTriplet([1,2]))
# print(solution.increasingTriplet([1,2,3]))
# print(solution.increasingTriplet([3,2,1]))
# print(solution.increasingTriplet([1,1,1]))
# print(solution.increasingTriplet([0,0,1,2,3]))
# print(solution.increasingTriplet([4, 2, 3, 3, 1, 4, 3]))
# print(solution.increasingTriplet([0,2,3,0,1,4,3]))
print(solution.increasingTriplet([9, 8, 7, 3, 4, 5, 0, 1, 0]))
print(solution.increasingTriplet([1, 2, 2, 2, 2, 2, 3]))
print(solution.increasingTriplet([9, 1, 8, 2, 7, 3]))
print(solution.increasingTriplet([9, 8, 1]))
print(solution.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

