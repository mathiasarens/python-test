class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        current_lower = lower
        def check(num, lower_num, upper_num):
            if num > lower_num+1 and num <= upper_num:
                if num - lower_num - 2 == 0:
                    ans.append(str(num-1))
                elif num-lower_num-2 > 0:
                    ans.append(str(lower_num+1)+"->"+str(num-1))
                else:
                    print("Should not happen " + str(num) + " " + str(lower_num))

        for index, num in enumerate(nums):
            if index == 0 and num>lower:
                check(num, lower-1, upper)
            else:    
                check(num, current_lower, upper)
            current_lower = num
        if len(nums) == 0:
            check(upper+1, lower-1, upper+1)
        else:
            check(upper+1, current_lower, upper+1)
        return ans

solution = Solution()
print(solution.findMissingRanges([0, 1, 3, 50, 75], 0,99) == ["2", "4->49", "51->74", "76->99"])
print(solution.findMissingRanges([0, 1, 3, 50, 75], 0,50) == ["2", "4->49"])
print(solution.findMissingRanges([], 1,1) == ["1"])
print(solution.findMissingRanges([],-3,-1) == ["-3->-1"])
print(solution.findMissingRanges([-1],-2,-1) == ["-2"])

