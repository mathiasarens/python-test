import sys
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        result = [-10000000000000000]*(len(nums)+1)
        result[1] = nums[0]
        for i in range(1,len(nums)):
            value = result[i] + nums[i]
            if value > nums[i]:
                result[i+1] = value
            else:
                result[i+1] = nums[i]
        return max(result)

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([]))
print(solution.maxSubArray([-1]))
print(solution.maxSubArray([3,-1,5]))