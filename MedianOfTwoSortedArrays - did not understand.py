class Solution:
    def medianOfSortedArray(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums)%2==0:
            middle = len(nums)//2
            return (nums[middle-1]+nums[middle])/2
        else:
            middle = len(nums)//2
            return nums[middle]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median1 = self.medianOfSortedArray(nums1)
        median2 = self.medianOfSortedArray(nums2)
        if median1 != 0 and median2 != 0:
            return (median1+median2)/2
        elif median1 == 0:
            return median2
        elif median2 == 0:
            return median1

solution = Solution()
print("Median for [1,3],[2]", solution.findMedianSortedArrays([1,3],[2]))
print("Median for [1,2],[3,4]", solution.findMedianSortedArrays([1,2],[3,4]))
print("Median for [],[1]", solution.findMedianSortedArrays([],[1]))
print("Median for [3],[-2,-1]", solution.findMedianSortedArrays([3],[-2,-1]))