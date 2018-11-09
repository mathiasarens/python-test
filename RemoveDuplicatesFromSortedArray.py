
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        pos = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[pos]:
                if pos+1 != i:
                    pos+=1
                    nums[pos] = nums[i]
                else:
                    pos+=1
        return pos+1

solution = Solution()
print(solution.removeDuplicates([]))
print(solution.removeDuplicates([1]))
print(solution.removeDuplicates([0,0,0,0,0]))
print(solution.removeDuplicates([0,1,2,3,4]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))