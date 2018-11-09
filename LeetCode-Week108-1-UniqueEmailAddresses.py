class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            simplified_email = ""
            at_found = False
            plus_found = False
            for j in range(len(email)):
                if at_found:
                    simplified_email += email[j]
                else:
                    if email[j] == '@':
                        at_found = True
                        simplified_email += email[j]
                    elif email[j] == '+':
                        plus_found = True
                    elif email[j] != '.' and not plus_found:
                        simplified_email += email[j]
            result.add(simplified_email)
        return len(result)

solution=Solution()
print(solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(solution.numUniqueEmails([".email+alex@leetcode.com","..e.mail+bob.cathy@leetcode.com"]))
print(solution.numUniqueEmails(["testemail+david@lee.tco+de.com","testemail+david@lee.tco+dee.com"]))
print(solution.numUniqueEmails([]))
