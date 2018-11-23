import math
# Complete the decibinaryNumbers function below.
def decibinaryNumbers(x):
    decibinary_numbers_with_decimal = []
    for i in range(10**math.ceil(math.log2(x))):
        decibinary_numbers_with_decimal.append(calculate_decimal_from_deci_binary(i))
    decibinary_numbers_with_decimal.sort(key = lambda x: x[1])
    # for tuple in decibinary_numbers_with_decimal:
    #     print(f"{tuple[0]} {tuple[1]}")
    return decibinary_numbers_with_decimal[x-1][0]

def calculate_decimal_from_deci_binary(decibinary):
    decibinary_str = str(decibinary)
    length = len(decibinary_str)
    decimal_result = 0 
    for i in range(length):
        decimal_result += int(decibinary_str[i])*2**(length-1-i)
    return (decibinary,decimal_result)

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
# decibinaryNumbers(1)

testcase(0)
testcase(1)
# testcase(2)

