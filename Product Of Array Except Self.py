class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for i in range(len(nums))]
        temp = nums[0]
        for i in range(1, len(nums)):
            result[i] = temp
            temp*=nums[i]
        temp  = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            result[i] *= temp
            temp*= nums[i]
        return result

    def productExceptSelfWithDevision(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        for num in nums:
            product*=num
        result = []
        for num in nums:
            result.append(product//num)
        return result

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]) == solution.productExceptSelfWithDevision([1,2,3,4]))
print(solution.productExceptSelf([4,3,2,1]) == solution.productExceptSelfWithDevision([4,3,2,1]))
print(solution.productExceptSelf([4,3,2,1])) # [6,8,12,24]
                                             # 0, 1, 12,123
                                             # 234 34 ,4,  0
                                             #    0,     1, 12, 123, 1234
                                             # 2345,   345,  45,   5     0
print(solution.productExceptSelfWithDevision([4,3,2,1]))


# Division is not allowed
# class Solution:
#     