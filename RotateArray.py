class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k<1 and len(nums)<1 and k < len(nums):
            return
        nums_size = len(nums)
        k_true = k % nums_size
        arr = nums[nums_size-k_true:nums_size]
        nums[k_true:nums_size]=nums[0:nums_size-k_true]
        nums[0:k_true]=arr[0:len(arr)]

solution = Solution()
arr = [1,2,3,4,5,6,7]
solution.rotate(arr, 6)
print(arr)