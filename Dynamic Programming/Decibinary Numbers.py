import math
# Complete the decibinaryNumbers function below.
def decibinaryNumbers(x):
    result = []
    i = 0
    while len(result) < x:
        result.extend(array_of_decibinary_numbers_for_x_decimal(i))
        i+=1
    return result[x-1]

def array_of_decibinary_numbers_for_x_decimal(x):
    if x == 0:
        return [0]
    result = list(map(lambda x: int(x), array_of_decibinary_numbers_for_x_decimal_and_max_exponent(x,math.floor(math.log2(x)))))
    result.reverse()
    return result

def array_of_decibinary_numbers_for_x_decimal_and_max_exponent(x, exponent):
    if exponent < 0 or x <= 0:
        return []
    if exponent == 0 and 0 <= x <= 9:
        return [str(x)]
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

# print(array_of_decibinary_numbers_for_x_decimal(8))
# print(array_of_decibinary_numbers_for_x_decimal(5))

def testcase(i):
    print(f"TestCase{i}")
    fptr_input = open(f"Dynamic Programming/Decibinary Numbers-TestCase{i}.txt", 'r')
    fptr_solution = open(f"Dynamic Programming/Decibinary Numbers-Solution{i}.txt", 'r')
    q = int(fptr_input.readline())
    for q_itr in range(q):
        x = int(fptr_input.readline())

        result = decibinaryNumbers(x)
        expected_result = int(fptr_solution.readline())
        print(result == expected_result)
        
    fptr_solution.close()
    fptr_input.close()
    print("")

# print(math.log2(32))
# print(math.log2(5))
# print(math.log2(8))
# print(math.floor(math.log2(8)))
# print(decibinaryNumbers(10))

testcase(0)
testcase(1)
testcase(2)

def decibinaryNumbersVerySlow(x):
    decibinary_numbers_with_decimal = []
    for i in range(10**math.ceil(math.log2(x))):
        decibinary_numbers_with_decimal.append(calculate_decimal_from_deci_binary(i))
    decibinary_numbers_with_decimal.sort(key = lambda x: x[1])
    for tuple in decibinary_numbers_with_decimal:
        print(f"{tuple[0]} {tuple[1]}")
    return decibinary_numbers_with_decimal[x-1][0]

def calculate_decimal_from_deci_binary(decibinary):
    decibinary_str = str(decibinary)
    length = len(decibinary_str)
    decimal_result = 0 
    for i in range(length):
        decimal_result += int(decibinary_str[i])*2**(length-1-i)
    return (decibinary,decimal_result)

