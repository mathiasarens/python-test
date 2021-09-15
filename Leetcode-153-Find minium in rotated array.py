from typing import List


class Solution:
    def findMinGood(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1 
        
        if nums[left] > nums[right]:
            while right - left > 1:
                mid = left + (right - left) // 2
                #print(nums[left], nums[mid], nums[right])
                if nums[mid] > nums[right]:
                    left = mid
                elif nums[left] > nums[mid]:
                    right = mid
            return nums[right]
        else:
            return nums[0]

x = Solution()
print('Solution: 0==', x.findMin([4,5,6,7,0,1,2]))
print('Solution: 0==', x.findMin([7,0,1,2,4,5,6]))
print('Solution: 0==', x.findMin([0,1,2,4,5,6,7]))
print('Solution: 0==', x.findMin([0]))