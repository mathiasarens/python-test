
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <1:
            return 0
        count_seq = [0] * len(nums)
        count_seq[0] = 0
        for i in range(len(nums)):
            maximum_length = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    maximum_length = max(count_seq[j], maximum_length)
            count_seq[i] = maximum_length+1
        return max(count_seq)

soltion = Solution()
print(soltion.lengthOfLIS([10,9,2,5,3,7,101,18])==4)
print(soltion.lengthOfLIS([10]))
print(soltion.lengthOfLIS([10,9,8,7,6,5,4,3,2,1]))
print(soltion.lengthOfLIS([]))
    