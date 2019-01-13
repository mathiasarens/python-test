# https://www.hackerrank.com/contests/saggezza-coding-test/challenges/insertionsort1
def insertionSort1(n, arr):
    i = n-1
    unsorted_value = arr[i]
    while i>0 and arr[i-1] > unsorted_value:
        arr[i] = arr[i-1]
        print(" ".join(map(lambda value: str(value), arr)))
        i-=1
    arr[i] = unsorted_value
    print(" ".join(map(lambda value: str(value), arr)))

insertionSort1(5, [2,4,6,8,3])
print()
insertionSort1(1, [2])