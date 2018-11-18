class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        peak = False
        for i in range(1,len(A)):
            if A[i-1] >= A[i] and i == 1:
                return False
            elif A[i-1] > A[i] and not peak:
                peak = True
            elif A[i-1] <= A[i] and peak:
                return False
        return peak

solution = Solution()
print(solution.validMountainArray([2,1])==False)
print(solution.validMountainArray([2,4,3])== True)
print(solution.validMountainArray([2,1,3])== False)
print(solution.validMountainArray([3,5,5])==False)
print(solution.validMountainArray([3,4,5])==False)
print(solution.validMountainArray([3,4,2])==True)
print(solution.validMountainArray([3,4,2,4])==False)
print(solution.validMountainArray([1,1,1])==False)
print(solution.validMountainArray([1,1,1,1,3,2])==False)
print(solution.validMountainArray([3,7,6,4,3,0,1,0])==False)
print(solution.validMountainArray([2,1,2,3,5,7,9,10,12,14,15,16,18,14,13])==False)
print(solution.validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3])==False)