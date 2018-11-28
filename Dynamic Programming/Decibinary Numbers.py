# Solution from https://github.com/charles-wangkai/hackerrank/blob/master/decibinary-numbers/Solution.java
import math
import bisect

class Solution:
    LIMIT_EXPONENT=19
    LIMIT_DECIMAL_NUMBERS=30000

    def __init__(self):
        self.count_decibinary_number_per_exponent = [[0 for i in range(self.LIMIT_DECIMAL_NUMBERS+1)] for i in range(self.LIMIT_EXPONENT+1)]
        self.sum_count_decibinary_numbers = [0 for i in range(self.LIMIT_DECIMAL_NUMBERS+1)]
        self.calculate_count_decibinary_numbers()
        self.calculate_sum_count_decibinary_numbers()

    def calculate_count_decibinary_numbers(self):
        self.count_decibinary_number_per_exponent[0][0]=1
        for e in range(1,self.LIMIT_EXPONENT+1):
            for s in range(self.LIMIT_DECIMAL_NUMBERS+1):
                for i in range(0,10):
                    nextS = s - i * (2**(e-1))
                    if nextS >= 0:
                        self.count_decibinary_number_per_exponent[e][s]+=self.count_decibinary_number_per_exponent[e-1][nextS]    

    def calculate_sum_count_decibinary_numbers(self):
        curr = 0
        for i in range(self.LIMIT_DECIMAL_NUMBERS+1):
            curr += self.count_decibinary_number_per_exponent[self.LIMIT_EXPONENT][i]
            self.sum_count_decibinary_numbers[i] = curr

    # Complete the decibinaryNumbers function below.
    def decibinaryNumbers(self, x):
        decimal_number = bisect.bisect_left(self.sum_count_decibinary_numbers, x)
        if decimal_number == 0:
            index1_of_decibinary_number_at_decimal = x
        else:
            index1_of_decibinary_number_at_decimal = x - self.sum_count_decibinary_numbers[decimal_number-1]
        result = []
        for exponent in range(self.LIMIT_EXPONENT,0,-1):
            prev_index = -1
            index = 0
            digit = -1
            while index < index1_of_decibinary_number_at_decimal:
                digit +=1
                prev_index = index
                index += self.count_decibinary_number_per_exponent[exponent-1][decimal_number-digit*(2**(exponent-1))]
            result.append(digit)
            decimal_number-=digit*(2**(exponent-1))
            index1_of_decibinary_number_at_decimal-=prev_index
        return int(''.join(map(lambda x: str(x),result)))


# solution = Solution()
# print(solution.decibinaryNumbers(32))

# for i in range(1,21):
#     print(f"{i}: {calculate_count_decibinary_numbers_recursive(i)}")
# print(array_of_decibinary_numbers_for_x_decimal(5))
# print(array_of_decibinary_numbers_for_x_decimal(10))

def testcase(i):
    print(f"TestCase{i}")
    fptr_input = open(f"Dynamic Programming/Decibinary Numbers-TestCase{i}.txt", 'r')
    fptr_solution = open(f"Dynamic Programming/Decibinary Numbers-Solution{i}.txt", 'r')
    solution = Solution()
    q = int(fptr_input.readline())
    for q_itr in range(q):
        x = int(fptr_input.readline())

        result = solution.decibinaryNumbers(x)
        expected_result = int(fptr_solution.readline())
        if result != expected_result:
            print(f"testcase: {x}: expected: {expected_result} but got: {result}")
            break
        
    fptr_solution.close()
    fptr_input.close()
    print("All tests ok")
    print("")

# print(math.log2(32))
# print(math.log2(5))
# print(math.log2(8))
# print(math.floor(math.log2(8)))
# print(decibinaryNumbers(42))
# print(decibinaryNumbers(49) == 34)

testcase(0)
testcase(1)
testcase(2)
testcase(3)
testcase(4)

def calculate_count_decibinary_numbers_recursive(x):
    return calculate_count_decibinary_numbers_recursive_inner(x, math.floor(math.log2(x)))

def calculate_count_decibinary_numbers_recursive_inner(x, e):
    if e < 0:
        if x == 0:
            return 1
        else: 
            return 0
    result = 0
    for i in range(0,10):
        rest = x - i * (2**e)
        if rest >= 0:
            result += calculate_count_decibinary_numbers_recursive_inner(rest, e-1)
    return result


# Solution 2 still to slow

def decibinaryNumbersTooSlow(x):
    result = []
    i = 0
    while len(result) < x:
        result.extend(map(lambda x: (x, i),array_of_decibinary_numbers_for_x_decimal(i)))
        i+=1
    for index, tuple in enumerate(result):
        print(f"{index+1}: {tuple[0]} {tuple[1]}")
    return result[x-1][0]

def array_of_decibinary_numbers_for_x_decimal(x):
    if x == 0:
        return [0]
    result = list(map(lambda x: int(x), array_of_decibinary_numbers_for_x_decimal_and_max_exponent(x,math.floor(math.log2(x)))))
    result.reverse()
    return result

def array_of_decibinary_numbers_for_x_decimal_and_max_exponent(x, exponent):
    if exponent < 0 or x <= 0:
        return []
    if exponent == 0:
        if 0 <= x <= 9:
            return [str(x)]
        else: 
            return []
    result = []
    for j in range(math.ceil(x/2**exponent)+1,0,-1):
        rest = x - (j * 2**exponent) 
        if rest == 0:
            result.append(str(j) + ''.join(["0" for i in range(exponent)]))
        elif rest > 0:
            rest_results = array_of_decibinary_numbers_for_x_decimal_and_max_exponent(rest,exponent-1)
            for rest_result in rest_results:
                result.append(str(j) + rest_result.zfill(exponent))
    other_results = array_of_decibinary_numbers_for_x_decimal_and_max_exponent(x,exponent-1)
    for other_result in other_results:
        result.append(other_result.zfill(exponent))
    return result

# decibinaryNumbersTooSlow(42)

# for i in range(21): 
#     print(f"{i}: {array_of_decibinary_numbers_for_x_decimal(i)}")
# for i in range(100):
#     print(f"{i}: {len(array_of_decibinary_numbers_for_x_decimal(i))}")


# print(f"{3}: {array_of_decibinary_numbers_for_x_decimal(3)}")
# print(f"{8}: {array_of_decibinary_numbers_for_x_decimal(8)}")
# print(f"{20}: {array_of_decibinary_numbers_for_x_decimal(20)}")
# print(f"{27}: {array_of_decibinary_numbers_for_x_decimal(27)}")
# print(f"{28}: {array_of_decibinary_numbers_for_x_decimal(28)}")
# print(f"{136}: {array_of_decibinary_numbers_for_x_decimal(136)}")

# print(f"{27}: {len(array_of_decibinary_numbers_for_x_decimal(27))}")
# print(f"{28}: {len(array_of_decibinary_numbers_for_x_decimal(28))}")



# Solution 1 - very slow

def decibinaryNumbersVerySlow(x):
    decibinary_numbers_with_decimal = []
    for i in range(10**math.ceil(math.log2(x))):
        decibinary_numbers_with_decimal.append(calculate_decimal_from_deci_binary(i))
    decibinary_numbers_with_decimal.sort(key = lambda x: x[1])
    for index, tuple in enumerate(decibinary_numbers_with_decimal):
        print(f"{index+1}: {tuple[0]} {tuple[1]}")
    return decibinary_numbers_with_decimal[x-1][0]

def calculate_decimal_from_deci_binary(decibinary):
    decibinary_str = str(decibinary)
    length = len(decibinary_str)
    decimal_result = 0 
    for i in range(length):
        decimal_result += int(decibinary_str[i])*2**(length-1-i)
    return (decibinary,decimal_result)

# decibinaryNumbersVerySlow(42)