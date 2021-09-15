from typing import List
import collections

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
       frequency_dict = collections.Counter(nums)
       return sorted(nums, key=lambda x: (frequency_dict[x], -x))

s = Solution()
print('[1,1,2,2,2,3] => ',s.frequencySort([1,1,2,2,2,3]))
print('[2,3,1,3,2] => ',s.frequencySort([2,3,1,3,2]))
