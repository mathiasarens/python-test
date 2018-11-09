from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        d=defaultdict(lambda:0)
        ps=0
        ans=0
        for a in A:
            d[ps]+=1
            ps+=a
            ans+=d[ps-S]
        return ans


solution=Solution()
print(solution.numSubarraysWithSum([1,0,1,0,1],2))
