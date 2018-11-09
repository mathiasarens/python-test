class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        abs_a = abs(a)
        abs_b = abs(b)
        sign = 1
        max_binary_length = max(len(format(abs_a,"b")), len(format(abs_b,"b")))+2
        bin_a = list(map(lambda x: int(x), format(abs_a, "0{}b".format(max_binary_length))))
        bin_b = list(map(lambda x: int(x), format(abs_b, "0{}b".format(max_binary_length))))
        if a >= 0 and b >= 0:
            bin_sum = self._add(bin_a, bin_b)
        elif a < 0 and b < 0:
            bin_sum = self._add(bin_a, bin_b)
            sign = -1
        elif a >= 0 and b < 0:
            if abs_a >= abs_b:
                bin_sum = self.__substract(bin_a, bin_b)
            else:
                bin_sum = self.__substract(bin_b,bin_a)
                sign = -1
        else:
            if abs_a >= abs_b:
                bin_sum = self.__substract(bin_a, bin_b)
                sign = -1
            else:
                bin_sum = self.__substract(bin_b, bin_a)
        
        return sign * self._convertBinaryArrayToNumber(bin_sum)

    def __substract(self, bin_a, bin_b):
        bin_substract = self._add(bin_a, self.__complement(bin_b))
        # remove highest bit
        bin_substract[0] = 0
        return bin_substract

    def __complement(self, bin_value):
        for i in range(1,len(bin_value)):
            if bin_value[i] == 0:
                bin_value[i] = 1
            else:
                bin_value[i] = 0
        
        bin_value = self._add(bin_value, self.__createBin1(len(bin_value)))
        return bin_value

    def __createBin1(self, length_value):
        bin_1 = [0] * length_value
        bin_1[length_value-1]=1
        return bin_1

    def _add(self, bin_a, bin_b):
        bin_sum = [0] * len(bin_a)
        carry = 0
        for i in range(len(bin_sum)-1, -1, -1):
            bin_sum[i] = bin_a[i] ^ bin_b[i]
            bin_sum[i] = bin_sum[i] ^ carry
            carry = bin_a[i] & bin_b[i] or ((bin_a[i] ^ bin_b[i]) and carry)
        return bin_sum

    def _convertBinaryArrayToNumber(self, arr):
        result = 0
        for i in range(len(arr)-1, -1, -1):
            result+=arr[i] * pow(2, len(arr)-i-1)
        return result




solution = Solution()
print(solution.getSum(1,1) == 2)
print(solution.getSum(-1,1)==0)
print(solution.getSum(-1,-1)==-2)
print(solution.getSum(-8,-1)==-9)
print(solution.getSum(8,-1)==7)
print(solution.getSum(-8,1)==-7)
print(solution.getSum(1,8)==9)
print(solution.getSum(1,-8)==-7)
print(solution.getSum(-1,8)==7)
print(solution.getSum(-1,-8)==-9)
print(solution.getSum(-1,0)==-1)
print(solution.getSum(0,0)==0)
print(solution.getSum(0,-1)==-1)
print(solution.getSum(0,0)==0)
print(solution.getSum(-2,-1)==-3)
print(solution.getSum(15,1)==16)
print(solution.getSum(2147483647,-2147483648)==-1)
print(solution.getSum(2147483646,1)==2147483647)
# Overflows not validated
# print(solution.getSum(2147483647,1)==-2147483648)
# print(solution.getSum(2147483648,1)==-2147483647)

