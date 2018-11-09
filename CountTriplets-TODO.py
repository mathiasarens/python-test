from collections import defaultdict
import math
import os
import random
import re
import sys

def countTriplets(arr, r):
    # count_dict = defaultdict(lambda: [0]*3)
    # for value in arr:
    #     count_dict[value][2] += count_dict[value//r][1]
    #     count_dict[value][1] += count_dict[value//r][0]
    #     count_dict[value][0] += 1
    # sum = 0
    # for key, value in count_dict.items():
    #     sum += value[2]
    # return sum
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
    return count


print(countTriplets([1, 2, 2, 4], 2) == 2)
# print(countTriplets([1, 2, 2, 4, 4], 2) == 4)
# print(countTriplets([1, 2, 2, 4, 4, 4], 2) == 6)
# print(countTriplets([1, 2, 1, 2, 4], 2) == 3)
# print(countTriplets([4, 8, 16, 32], 2) == 2)
# print(countTriplets([1, 4, 16, 64], 4) == 2)
# print(countTriplets([1, 4, 16, 256], 4) == 1)
# print(countTriplets([1, 4, 64, 256], 4) == 0)
# print(countTriplets([1, 16, 64, 256], 4) == 1)
# print(countTriplets([1, 3, 9, 9, 27, 81], 3) == 6)
# print(countTriplets([1, 5, 5, 25, 125], 5) == 4)
# print(countTriplets([1], 5) == 0)
# print(countTriplets([1, 2, 4], 2) == 1)
# print(countTriplets([1, 4, 12, 16], 4) == 1)
# print(countTriplets([1], 1) == 0)
# print(countTriplets([1,1], 1) == 0)
# print(countTriplets([1,1,1], 1) == 1)
# print(countTriplets([1,1,1,1], 1) == 4)
# print(countTriplets([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],1) == 161700)

# fptr = open('CountTriplets-TestCase6.txt', 'r')
# nr = fptr.readline().rstrip().split()
# n = int(nr[0])
# r = int(nr[1])
# arr = list(map(int, fptr.readline().rstrip().split()))
# fptr.close()
# ans = countTriplets(arr, r)
# print("actual: " + str(ans) +  ", expected: 2325652489; maxsize: " + str(sys.maxsize))

