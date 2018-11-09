import sys

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        costs_of_flipping_1_to_0 = [0] * (len(S)+1)
        for i in range(0,len(costs_of_flipping_1_to_0)-1):
            costs_of_flipping_1_to_0[i+1] = costs_of_flipping_1_to_0[i] + (1 if i < len(S) and S[i]=='1' else 0)
        costs_of_flipping_0_to_1 = [0] * (len(S)+1)
        for i in range(len(costs_of_flipping_0_to_1),1,-1):
            costs_of_flipping_0_to_1[i-2] = costs_of_flipping_0_to_1[i-1] + (1 if i >= 2 and S[i-2]=='0' else 0)
        min_costs_of_flipping = sys.maxsize
        for i in range(0, len(S)+1):
            min_costs_of_flipping = min(min_costs_of_flipping, costs_of_flipping_1_to_0[i]+costs_of_flipping_0_to_1[i])
        return min_costs_of_flipping



solution=Solution()
print(solution.minFlipsMonoIncr("00110"))
print(solution.minFlipsMonoIncr("010110"))
print(solution.minFlipsMonoIncr("00011000"))

#  00110
# 000122
# 321110
# 321232

