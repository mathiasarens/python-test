import sys

def solution(nums):
    # find degree of array

    frequencies = {}
    smallest_index = {}
    largest_index = {}

    for i in range(len(nums)):
        if nums[i] in frequencies:
            frequencies[nums[i]] += 1
            largest_index[nums[i]] = i
        else:
            frequencies[nums[i]] = 1
            smallest_index[nums[i]] = i
            largest_index[nums[i]] = i

    maximum_frequency = 0
    maximum_frequency_number = 0
    minimum_length_of_subarray = sys.maxsize
    for number, frequency in frequencies.items():
        sub_array_size = largest_index.get(number, 0) - smallest_index.get(number, 0) +1
        if (frequency>maximum_frequency or (frequency == maximum_frequency and sub_array_size < minimum_length_of_subarray)):
            maximum_frequency = frequency
            maximum_frequency_number = number
            minimum_length_of_subarray = sub_array_size

    if minimum_length_of_subarray == sys.maxsize:
        return 0
    else:
        return minimum_length_of_subarray

print(solution([]))
print(solution([1]))
print(solution([1,1]))
print(solution([2,1]))
print(solution([1,2,2,3,1]))
print(solution([1,2,2,3,1,4,2]))