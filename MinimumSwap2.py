
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    sorted_array = sorted(arr)
    minimum_swaps = len(arr)+10
    minimum_swaps = min(minimum_swaps, calculateMinimumSwap(arr[:], sorted_array, createValueToIndexMap(arr)))
    return minimum_swaps

def swap(arr, x, y):
    buffer = arr[y]
    arr[y] = arr[x]
    arr[x] = buffer

def calculateMinimumSwap(arr, sortedArray, valueToIndexMap):
    swaps = 0
    for i in range(len(arr)):
        if sortedArray[i] != arr[i]:
            from_pos = valueToIndexMap[sortedArray[i]]
            wrong_value = arr[i]
            swap(arr, from_pos, i)
            valueToIndexMap[wrong_value] = from_pos
            swaps+=1
    return swaps

def createValueToIndexMap(arr):
    valueToIndexDict = {}
    for i in range(len(arr)):
        valueToIndexDict[arr[i]] = i
    return valueToIndexDict

# print(minimumSwaps([1,3,5,2,4,6,8])==3)
print(minimumSwaps([4,3,1,2])==3)

