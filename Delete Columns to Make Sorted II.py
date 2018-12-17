class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        i = 1
        c = 0
        while i < len(A) and len(A[0])>0:
            j = 0
            while j < len(A[i-1]) and A[i-1][j] == A[i][j]:
                j+=1
            if j < len(A[i-1]) and A[i-1][j] > A[i][j]:
                i = 1
                c+=1
                for k in range(len(A)):
                    A[k] = A[k][:j]+A[k][j+1:]
            else:
                i+=1
        return c

solution = Solution()
print(solution.minDeletionSize(["ca","bb","ac"])==1)
print(solution.minDeletionSize(["xc","yb","za"])==0)
print(solution.minDeletionSize(["zyx","wvu","tsr"])==3)
print(solution.minDeletionSize(["xga","xfb","yfa"])==1)
print(solution.minDeletionSize(["xga"])==0)
print(solution.minDeletionSize(["xgb","xga"])==1)