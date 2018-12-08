from collections import defaultdict
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = [None] * (len(A) * len(B))
        CD = [None] * (len(C) * len(D))
        k = 0
        for i in range(len(A)):
            for j in range(len(B)):
                AB[k] = A[i]+B[j]
                CD[k] = C[i]+D[j]
                k+=1
        counterpart_AB = defaultdict(int)
        for i in range(len(AB)):
            counterpart_AB[0-AB[i]]+=1
        c = 0
        for i in range(len(CD)):
            c+=counterpart_AB[CD[i]]
        return c
    
solution = Solution()
print(solution.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])==2)
print(solution.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1])==6)