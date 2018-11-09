class Solution:

    def expandAroundCenter(self, s, L, R):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s)<1:
            return ""
        max_start = 0
        max_end = 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            if len1 > max_end - max_start:
                max_start = i - len1 // 2
                max_end = i + len1 // 2
            if len2 > max_end-max_start:
                max_start = i - (len2-1) // 2
                max_end = i + len2 // 2
        return s[max_start:max_end+1]

solution = Solution()
print(solution.longestPalindrome("babad")=="aba") #bab or aba
print(solution.longestPalindrome("cbbd")=="bb") #bb
print(solution.longestPalindrome("a")=="a") #a
print(solution.longestPalindrome("aa")=="aa") #aa
print(solution.longestPalindrome("aaa")=="aaa") #aaa
print(solution.longestPalindrome("aaaa")=="aaaa") #aaaa
print(solution.longestPalindrome("vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy") == "oxaxo") #oxaxo