class DSU(object):
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [0]*1001
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    
    def union(self, x, y):
        xr,yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True
            
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge

solution = Solution()
print(solution.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(solution.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))