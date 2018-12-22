import math
import collections

class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.par[xr] = yr

class Solution(object):
    def largestComponentSize(self, A):
        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1

            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())

solution = Solution()
assert(solution.largestComponentSize([4,6,15,35]) == 4)
assert(solution.largestComponentSize([20,50,9,63]) == 2)
assert(solution.largestComponentSize([2,3,6,7,4,12,21,39]) == 8)
assert(solution.largestComponentSize([99,100,69,39,14,56,91,60]) == 8)
        
# class DSU:
#     def __init__(self, N):
#         self.par = list(range(N))
#         self.size = [1]*N
#         self.maximum = 0

#     def find(self, x):
#         if self.par[x] != x:
#             self.par[x] = self.find(self.par[x])
#         return self.par[x]

#     def union(self, x, y):
#         xr, yr = self.find(x), self.find(y)
#         if xr!=yr:
#             self.par[xr] = yr
#             self.size[yr] += self.size[xr]
#             self.maximum = max(self.maximum, self.size[yr])

# class Solution:
#     def largestComponentSize(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         factor_to_number_dict = {}
#         dsu = DSU(len(A))
#         for i in range(len(A)):
#             for j in range(2, math.floor(math.sqrt(A[i]))+1):
#                 if A[i]%j==0:
#                     if j in factor_to_number_dict:
#                         dsu.union(i, factor_to_number_dict[j])
#                     else:
#                         factor_to_number_dict[j] = i
#                     if A[i]//j in factor_to_number_dict:
#                         dsu.union(i, factor_to_number_dict[A[i]//j])
#                     else:
#                         factor_to_number_dict[A[i]//j] = i
#             # A[i] can be a factor, too
#             if A[i] in factor_to_number_dict:
#                 dsu.union(i, factor_to_number_dict[A[i]])
#             else:
#                 factor_to_number_dict[A[i]] = i
#         return dsu.maximum   