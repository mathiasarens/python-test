import bisect

## https://www.quora.com/What-is-the-logic-used-in-the-HackerRank-Maximise-Sum-problem

def maximumSum(a, m):
    max_modulo = 0
    prefix = []
    curr = 0
    for i in range(len(a)):
        curr = (a[i]%m + curr)%m
        insertion_pos = bisect.bisect_left(prefix, curr)
        prefix.insert(insertion_pos,curr)
        prefix_value_greater_curr = bisect.bisect_right(prefix,curr)
        if prefix_value_greater_curr < len(prefix):
            max_modulo = max(max_modulo, (curr-prefix[prefix_value_greater_curr] + m)%m)
        max_modulo = max(max_modulo, curr)
    return max_modulo

# print(maximumSum([3,3,9,9,5],7) == 6)
# print(maximumSum([1,2,3],2) == 1)
# print(maximumSum([3,7,11,17],16)==12)

def maximumSumSlowButCorrect(a, m):
    max_modulo = 0
    for sal in range(1,len(a)):
        for i in range(len(a)-sal+1):
            sum = 0
            for j in range(i, i+sal):
                sum += a[j]
            max_modulo = max(max_modulo, sum%m)
    return max_modulo

def maximumSumBruteForceWithModuloSumArray(a, m):
    max_modulo = 0
    prefix = [0 for i in range(len(a))]
    curr = 0
    for i in range(len(a)):
        curr = (a[i]%m + curr)%m
        prefix[i]=curr

    for i in range(len(a)):
        for j in range(i-1,-1,-1):
            max_modulo = max(max_modulo, (prefix[i]-prefix[j] + m)%m)
        max_modulo = max(max_modulo, prefix[i])

    print(prefix)
    print(max_modulo)
    return max_modulo

# if __name__ == '__main__':
#     testcase_input = open('Maximum SubArray Sum Modulo-TestCase1.txt', 'r')
#     testcase_result = open('Maximum SubArray Sum Modulo-Solution1.txt', 'r')
#     q = int(testcase_input.readline())
#     for q_itr in range(q):
#         nm = testcase_input.readline().split()
#         n = int(nm[0])
#         m = int(nm[1])
#         a = list(map(int, testcase_input.readline().rstrip().split()))
#         result = maximumSum(a, m)
#         expected_result = int(testcase_result.readline())
#         print(expected_result == result)
#     testcase_input.close()
#     testcase_result.close()
