class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S[0] == 0:
            return []
        for i in range(1,len(S)):
            for j in range(i+1,len(S)):
                try:
                    a = int(S[0:i])
                    b = int(S[i:j])
                    if a <= 2**31-1 and b <= 2**31-1:
                        result = self.split_into_fibonacci(S[j:len(S)], [a,b])
                        result_str = ""
                        for c in result:
                            result_str += str(c)
                        if result_str == S:
                            return result
                except ValueError:
                    pass
        return []


    def split_into_fibonacci(self, S, result):
        if len(S) == 0:
            return []
        number = result[-2] + result[-1]
        number_str = str(number)
        if number_str == S[0:len(number_str)] and number <= 2**31-1:
            result.append(number)
            self.split_into_fibonacci(S[len(number_str):len(S)], result)
        return result



solution = Solution()
# print(solution.splitIntoFibonacci("123456579")) # => [123,456,579]
# print(solution.splitIntoFibonacci("11235813")) # => [1,1,2,3,5,8,13]
# print(solution.splitIntoFibonacci("112358130")) # => [] The task is impossible.
# print(solution.splitIntoFibonacci("0123")) # => [] Leading zeroes are not allowed, so "01", "2", "3" is not valid.
# print(solution.splitIntoFibonacci("1101111")) # => [110, 1, 111] The output [11, 0, 11, 11] would also be accepted.
# print(solution.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")) # => []
