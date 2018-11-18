# Complete the countInversions function below.
def countInversions(arr):
    result = [None for i in range(len(arr))]
    return mergeSort(arr, result, 0, len(arr)-1)


def mergeSort(arr, result, left, right):
    if left >= right:
        return 0

    swaps = 0
    middle = (right+left)//2
    swaps += mergeSort(arr, result, left, middle)
    swaps += mergeSort(arr, result, middle+1, right)
    swaps += mergeHalves(arr, result, left, right)
    return swaps


def mergeHalves(arr, result, left_start, right_end):
    left_end = (right_end+left_start) // 2
    right_start = left_end+1

    left_index = left_start
    right_index = right_start
    index = left_start
    swaps = 0
    while(left_index <= left_end and right_index <= right_end):
        if arr[left_index] <= arr[right_index]:
            result[index] = arr[left_index]
            left_index += 1
        else:
            result[index] = arr[right_index]
            right_index += 1
            swaps += right_start - left_index
        index += 1
    result[index:index+left_end+1-left_index] = arr[left_index:left_end+1]
    result[index:index+right_end+1-right_index] = arr[right_index:right_end+1]
    arr[left_start:right_end+1] = result[left_start:right_end+1]
    return swaps


print(countInversions([1, 2]) == 0)
print(countInversions([2, 1]) == 1)
print(countInversions([2, 3, 1]) == 2)
print(countInversions([1, 2, 3]) == 0)
print(countInversions([3, 2, 1]) == 3)
print(countInversions([3, 1, 2]) == 2)
print(countInversions([1, 1, 1]) == 0)
print(countInversions([1]) == 0)
print(countInversions([1, -1]) == 1)
print(countInversions([1, -1, -5]) == 3)
