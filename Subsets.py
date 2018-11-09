class Solution:
    def subsets_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def backtracking(list_of_numbers = [],count=0):
            if count >= len(nums):
                result.append(list_of_numbers)
                return
            new_list_of_numbers_without_item = list_of_numbers[:]
            new_list_of_numbers_with_item = list_of_numbers[:]
            new_list_of_numbers_with_item.append(nums[count])
            backtracking(new_list_of_numbers_without_item, count+1)
            backtracking(new_list_of_numbers_with_item, count+1)
        backtracking()
        return result

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(pow(2,len(nums))):
            intermediate_result=[]
            for j,c in enumerate("{0:b}".format(i).zfill(len(nums))):
                if int(c) == 1:
                    intermediate_result.append(nums[j])
            result.append(intermediate_result)

        return result

solution = Solution()
# print(solution.subsets([]))
# print(solution.subsets([1]))
print(solution.subsets([1,2,3]))
                



# 1 2 3 4

# 123
# 124
# 134
# 234


# 12
# 13
# 14
# 23
# 24
# 34