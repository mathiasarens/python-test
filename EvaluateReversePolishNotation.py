class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result,i = self.evaluateReversePolishNotation(tokens, len(tokens)-1)
        return result
    
    def evaluateReversePolishNotation(self, tokens, i):
        # read next operands
        operators = ['*', '+', '-', '/']
        if tokens[i] not in operators:
            return (int(tokens[i]),i)
        operator = tokens[i]
        operand2 = 0
        operand2_index = 0
        if tokens[i-1] in operators:
            result, new_i = self.evaluateReversePolishNotation(tokens, i-1)
            operand2 = result
            operand2_index = new_i
        else:
            operand2 = int(tokens[i-1])
            operand2_index = i-1

        operand1 = 0
        operand1_index = 0
        if tokens[operand2_index-1] in operators:
            result, new_i = self.evaluateReversePolishNotation(tokens, operand2_index-1)
            operand1 = result
            operand1_index = new_i
        else:
            operand1 = int(tokens[operand2_index-1])
            operand1_index = operand2_index-1
        return (self.excute_operation(operand1, operand2, operator), min(operand2_index, operand1_index))

    def excute_operation(self, operator1, operator2, operator):
        if operator == '+':
            return operator1+operator2
        elif operator == '-':
            return operator1-operator2
        elif operator == '*':
            return operator1*operator2
        elif operator == '/':
            return int(operator1/operator2)
        else:
            raise Exception("unknown operator " + operator)

solution = Solution()
print(solution.evalRPN(["18"])==18)
print(solution.evalRPN(["2", "1", "+", "3", "*"])==9)
print(solution.evalRPN(["4", "13", "5", "/", "+"])==6)
print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])==22)