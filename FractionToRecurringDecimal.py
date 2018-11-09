class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return str(0)
        if denominator == 0:
            return "NaN"
        ans = ""
        if (numerator < 0) ^ (denominator < 0):
            ans += "-"
        denominator = abs(denominator)
        rest = abs(numerator)
        remainder_dict = {}
        is_fraction_part = False
        while rest != 0 and not remainder_dict.get(rest):
            if is_fraction_part:
                remainder_dict[rest] = len(ans)
            division_result = int(rest / denominator)
            ans += str(division_result)
            rest -= (division_result * denominator)
            if rest != 0 and not is_fraction_part:
                ans += "."
                is_fraction_part = True
            rest *= 10
        if remainder_dict.get(rest):
            ans = ans[0:remainder_dict[rest]] + "(" + ans[remainder_dict[rest]:] + ")"
        return ans
                

solution = Solution()
print(solution.fractionToDecimal(1,2) == "0.5")
print(solution.fractionToDecimal(2,1) == "2")
print(solution.fractionToDecimal(2,-1) == "-2")
print(solution.fractionToDecimal(-10,5) == "-2")
print(solution.fractionToDecimal(2,3) == "0.(6)")
print(solution.fractionToDecimal(1,6) == "0.1(6)")
print(solution.fractionToDecimal(12,11) == "1.(09)")
print(solution.fractionToDecimal(11,12) == "0.91(6)")
print(solution.fractionToDecimal(0,3) == "0")
print(solution.fractionToDecimal(-50,8) == "-6.25")
print(solution.fractionToDecimal(7,-12) == "-0.58(3)")
print(solution.fractionToDecimal(7,0) == "NaN")
print(solution.fractionToDecimal(7,-12))