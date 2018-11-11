class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        number_logs = list(filter(lambda log: str.isdigit(log.split(" ")[1]), logs))
        string_logs = list(filter(lambda log: not str.isdigit(log.split(" ")[1]), logs))
        string_logs2 = sorted(string_logs, key=lambda log: log.split(" ")[1:] + log.split(" ")[0:1])
        return string_logs2 + number_logs 

solution = Solution()
print(solution.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(solution.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act car"]))