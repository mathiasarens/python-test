class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used_characters = {}
        max_length = 0
        i = 0
        j = 0
        while i <len(s) and j < len(s):
            if s[j] in used_characters.keys():
                del used_characters[s[i]]
                i+=1
            else:
                used_characters[s[j]] = 1
                j+=1
                max_length = max(j-i, max_length)
        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring(""))
print(solution.lengthOfLongestSubstring("b"))
print(solution.lengthOfLongestSubstring(" "))