import math
# Complete the decibinaryNumbers function below.
def decibinaryNumbers(x):
    if x < 1:
        return -1
    dp = {}
    dp[0] = [0]
    dp[1] = [1]

    result = [] 
    i = 0
    while len(result) <= x:
        result.extend(map(lambda x: (x, i),calculcate_decibinary_numbers_for_dp(dp,i)))
        i+=1
    # for index, tuple in enumerate(result):
    #     print(f"{index+1}: {tuple[0]} {tuple[1]}")
    return result[x-1][0]

def calculcate_decibinary_numbers_for_dp(dp, num_dec):
        result = []
        last_number = 0
        if num_dec > 1:
            for prev in dp[num_dec-1]:
                new_number_str = increment_decibinary(str(prev))
                new_number = int(new_number_str)
                if new_number > last_number:
                    result.append(int(new_number_str))
                    last_number = new_number
                if new_number_str[-1] == '2':
                    result.append(int(add_decibinary_for_new_zero(new_number_str)))
                if num_dec/2**math.floor(math.log2(num_dec)) == 1.0:
                    result.extend(add_top_numbers(result[-1]))
            dp[num_dec] = result
        else:
            result = dp[num_dec]
        return result
            

def add_top_numbers(last_number):
    result = []
    last_number_str = str(last_number)
    for i in range(len(last_number_str)-1, -1, -1):
        if last_number_str[i] == '2':
            if i > 0:
                new_number = int(last_number_str[:i-1] + str(int(last_number_str[i-1])+1) + ''.join(['0' for i in range(len(last_number_str)-i)]))
                result.append(new_number)
                result.extend(add_top_numbers(new_number))
            else:
                result.append(int('1' + ''.join(['0' for i in range(len(last_number_str)-i)])))
        elif last_number_str[i] != '0':
            break
    return result
            
def add_decibinary_for_new_zero(decibinary_str):
        return increment_decibinary(decibinary_str[:-1]) + '0'

def increment_decibinary(decibinary_str):
    result = []
    pos_smaller_9 = len(decibinary_str)-1
    while pos_smaller_9 >=0:
        number = int(decibinary_str[pos_smaller_9])
        if number < 9:
            break
        pos_smaller_9-=1
    for i in range(pos_smaller_9):
        result.append(decibinary_str[i])
    largest_exponent = len(decibinary_str)-pos_smaller_9-1
    if pos_smaller_9 <0:
        result.append(str(1))
    else:
        result.append(str(int(decibinary_str[pos_smaller_9])+1))
    rest = (2**largest_exponent-1)*9+1-(2**(largest_exponent))
    for i in range(pos_smaller_9+1,len(decibinary_str)):
        largest_exponent-=1
        times = rest // (2**largest_exponent)
        new_number_at_pos = min(9,times)
        result.append(str(new_number_at_pos))
        rest -= new_number_at_pos*(2**largest_exponent)
        
    return ''.join(result)

# print(increment_decibinary(8)=='9')
# print(increment_decibinary(9)=='18')
# print(increment_decibinary(10)=='11')
# print(increment_decibinary(19)=='28')
# print(increment_decibinary(29)=='38')
# print(increment_decibinary(89)=='98')
# print(increment_decibinary(99)=='196')
# print(increment_decibinary(199)=='296')
# print(increment_decibinary(999)=='1992') # 999 = 36+18+9=63; 8 + 36 + 18 + 2= 64
# print(increment_decibinary(1999)=='2992') # 1999 = 36+18+9=63; 8 + 36 + 18 + 2= 64
# print(increment_decibinary(9999)=='19960') # 9999 = 72+36+18+9=135; 16 + 72 + 36 + 12 + 0= 136
# print(increment_decibinary(119)=='128') # 129 = 15 128 = 16



        

# print(array_of_decibinary_numbers_for_x_decimal(8))
# print(array_of_decibinary_numbers_for_x_decimal(5))
# print(array_of_decibinary_numbers_for_x_decimal(10))

def testcase(i):
    print(f"TestCase{i}")
    fptr_input = open(f"Dynamic Programming/Decibinary Numbers-TestCase{i}.txt", 'r')
    fptr_solution = open(f"Dynamic Programming/Decibinary Numbers-Solution{i}.txt", 'r')
    q = int(fptr_input.readline())
    for q_itr in range(q):
        x = int(fptr_input.readline())

        result = decibinaryNumbers(x)
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

# testcase(0)
# testcase(1)
# testcase(2)
testcase(3)

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

# for i in range(11): 
#     print(f"{i}: {array_of_decibinary_numbers_for_x_decimal(i)}")
# for i in range(11):
#     print(f"{i}: {len(array_of_decibinary_numbers_for_x_decimal(i))}")

# print(f"{3}: {array_of_decibinary_numbers_for_x_decimal(3)}")
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

