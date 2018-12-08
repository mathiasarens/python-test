class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j =  len(height)-1
        max_container = 0
        while i < j:
            max_container = max(max_container, min(height[i], height[j]) * (j-i))
            if height[i]>height[j]:
                j-=1
            elif height[i]<=height[j]:
                i+=1
        return max_container

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])==49)
print(solution.maxArea([9,6,5,4,7,8])==40)
print(solution.maxArea([1,1,1,1,1,1,1])==6)
print(solution.maxArea([1,1,1,1,1,2,1])==6)
print(solution.maxArea([1,1,2,1,1,2,1])==6)
print(solution.maxArea([1,1,3,1,1,2,1])==6)
print(solution.maxArea([1,1,3,1,1,6,1])==9)
