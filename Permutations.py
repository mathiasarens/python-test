class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtracking(permutation_list=[], rest_list=nums):
            if len(permutation_list) >= len(nums):
                result.append(permutation_list)
                return
            
            for i in range(len(rest_list)):
                intermediate_new = permutation_list[:]
                intermediate_new.append(rest_list[i])
                rest_new = rest_list[:]
                rest_new.pop(i)
                backtracking(intermediate_new, rest_new)
        
        backtracking()
        return result

solution = Solution()
print(solution.permute([]))
print(solution.permute([1]))
print(solution.permute([1,2,3]))
print(solution.permute([6,5,4]))
print(solution.permute([6,5,4,3]))