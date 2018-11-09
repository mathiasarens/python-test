from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(lambda:0)
        for i in nums:
            d[i]+=1
        sorted_frequency_list = sorted(d.items(), key=lambda tup: tup[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_frequency_list[i][0])
        return result

solution = Solution()
# print(solution.topKFrequent([1], 1))
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1,1,1,2,2,3], 1))