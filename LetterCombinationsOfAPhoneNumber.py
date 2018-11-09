class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        letters_dict = {'2':'abc', '3':"def", '4':'ghi','5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for d in digits:
            next_result = []
            if d == '1' or d == '0':
                next_result = result
            else:
                for string in result:
                    for l in letters_dict[d]:
                        next_result.append(string+l)
            result = next_result
            if not result:
                if d != '1' and d != '0':
                    for l in letters_dict[d]:
                        result.append(l)   
            
        return result

solution = Solution()
# print(solution.letterCombinations(""))
# print(solution.letterCombinations("01"))
print(solution.letterCombinations("23"))
# print(solution.letterCombinations("213"))
# print(solution.letterCombinations("2130"))
# print(solution.letterCombinations("213000"))
# print(solution.letterCombinations("123"))
# print(solution.letterCombinations("791"))