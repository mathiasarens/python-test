from collections import defaultdict
import sys

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        char_dict = defaultdict(int)
        char_last_used_dict = {}
        
        for char in tasks:
            char_dict[char]+=1
            
        result = []
        while len(char_dict) > 0:
            char_dict_items = sorted(char_dict.items(), key=lambda x: x[1], reverse = True)
            slots_used = 0
            for i in range(n+1):
                if i < len(char_dict_items) and len(result) - char_last_used_dict.get(char_dict_items[i][0], -n-1) > n:
                    key = char_dict_items[i][0]
                    char_dict[key]-=1
                    if char_dict[key] <= 0:
                        del char_dict[key]
                    char_last_used_dict[key]=len(result)
                    result.append(key)
                    slots_used += 1
                elif len(char_dict) > 0:
                    result.append("idle")

        return len(result)
                
        
            
solution = Solution()
print(solution.leastInterval(["A","A","A","B","B","B"], 2) == 8)
print(solution.leastInterval(["A","B","B","B"], 2) == 7)
print(solution.leastInterval(["A","A","B","B","C","C"], 2) == 6)
print(solution.leastInterval(["A"], 3) == 1)
print(solution.leastInterval(["A"], 0) == 1)
print(solution.leastInterval([], 0) == 0)
print(solution.leastInterval(["A","A","A"], 3) == 9)
print(solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16)


# A A A A B B B B -> 2

# A 4      A:0
# B 4      B:1

# A B idle 

# A B B B

# ABiiBiiB
# BAiBiiB

# Brute force
# class Solution:
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         char_dict = defaultdict(int)
#         last_used = {}
        
#         for char in tasks:
#             char_dict[char]+=1
#         return self.leastIntervalRecursive(n, n, char_dict, last_used, [])

#     def leastIntervalRecursive(self, n, idle_count, char_dict, last_used, result_array):
#         if len(char_dict) == 0:
#             return len(result_array)
#         min_result = sys.maxsize
#         for k,v in char_dict.items():
#             if len(result_array)-last_used.get(k, -n-1)>n:
#                 new_char_dict = copy(char_dict)
#                 new_char_dict[k]-=1
#                 if new_char_dict[k] == 0:
#                     del new_char_dict[k]
#                 new_last_used = copy(last_used)
#                 new_last_used[k] = len(result_array)
#                 new_string = result_array[:]
#                 new_string.append(k)
#                 min_result = min(min_result, self.leastIntervalRecursive(n, n, new_char_dict, new_last_used, new_string))
#         # or idle
#         if idle_count > 0:
#             new_result_array = result_array[:]
#             new_result_array.append("idle")
#             min_result = min(min_result, self.leastIntervalRecursive(n, idle_count-1, char_dict, last_used, new_result_array))
#         return min_result