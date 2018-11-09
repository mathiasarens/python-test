class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtracking(S = '', left = 0, right = 0):
            if len(S) ==  2*n:
                result.append(S)
                return       
            if left < n:
                backtracking(S + '(', left+1, right)
            if right < left:
                backtracking(S+')', left, right+1)

        backtracking()
        return result

solution = Solution()
print(solution.generateParenthesis(0))
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(4))
# Expected: 14
# ["(((())))","((()()))","((())())","((()))()",
# "(()(()))","(()()())","(()())()","(())(())",
# "(())()()","()((()))","()(()())","()(())()",
# "()()(())","()()()()"]

# ['(((())))', '((()()))', '((())())', '((()))()', 
#  '(()(()))', '(()()())', '(()())()',             '()(())()', '(())()()', '()((()))', '()()(())', '()(()())',   , '()()()()',]
        
