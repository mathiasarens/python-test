from collections import Counter
class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort(key=lambda x: abs(x))
        double_value_dict = Counter(A)
        for i in range(len(A)):
            if double_value_dict[A[i]] > 0 and double_value_dict[2*A[i]]>0:
                if double_value_dict[A[i]]==1:
                    del double_value_dict[A[i]]
                elif double_value_dict[A[i]]>0:
                    double_value_dict[A[i]]-=1
                if double_value_dict[2*A[i]]==1:
                    del double_value_dict[2*A[i]]
                elif double_value_dict[2*A[i]]>0:
                    double_value_dict[2*A[i]]-=1
                
        return len(double_value_dict)==0

solution = Solution()
print(solution.canReorderDoubled([3,1,3,6])==False)
print(solution.canReorderDoubled([2,1,2,6])==False)
print(solution.canReorderDoubled([4,-2,2,-4])==True)
print(solution.canReorderDoubled([1,2,4,16,8,4])==False)
print(solution.canReorderDoubled([1,2])==True)
print(solution.canReorderDoubled([1,3])==False)
print(solution.canReorderDoubled([1,2,4,8])==True)