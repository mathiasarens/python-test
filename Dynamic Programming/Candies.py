def candies(n, arr):
    if len(arr) < 1:
        return 0
    candies_sum = 1
    last_peak_index = 0
    last_peak_candy = 1
    last_candy_amount = 1
    for i in range(1,len(arr)):
        # 3 2 / 5 3 2 1
        if arr[i-1] > arr[i]:
            last_candy_amount = 1
            candies_sum+=i-last_peak_index
            if i-last_peak_index >= last_peak_candy:
                last_peak_candy+=1
                candies_sum+=1
        elif arr[i-1] == arr[i]:
            last_candy_amount=1
            last_peak_index = i
            last_peak_candy = last_candy_amount
            candies_sum+=last_candy_amount
        # 1 2 2 / 1 2 3 / 1 2 1 / 2 3
        elif arr[i-1] < arr[i]:
            last_candy_amount+=1
            last_peak_index = i
            last_peak_candy = last_candy_amount
            candies_sum+=last_candy_amount
    return candies_sum
        


print(candies(3, [1, 2, 2]) == 4)
print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]) == 19)
print(candies(8, [2, 4, 3, 5, 2, 6, 4, 5]) == 12)
print(candies(8, [8,7,6,5,4,3,2,1])==36)
print(candies(8, [8,7,6,7,6,5,4])==16)
print(candies(8, [8,7,6,13,6,5,4])==16)
print(candies(0, [])==0)
print(candies(1, [12313123123])==1)
print(candies(2, [3,4])==3)
print(candies(2, [3,2])==3)
print(candies(2, [2,2])==2)
print(candies(2, [2,2,1])==4)
print(candies(2, [2,2,2,1])==5)
print(candies(3, [2,2,2])==3)
print(candies(3, [2,3,2,2,2])==6)
print(candies(2, [4,2,2,1])==6)
print(candies(2, [4,2,2,2,1])==7)
print(candies(2, [1,2,3,2,3])==9)
print(candies(2, [1,2,3,2,9,5,3,2])==17)

def testcase(i):
    fptr = open(f"Dynamic Programming/Candies-TestCase{i}.txt", 'r')
    n = int(fptr.readline())

    arr = []

    for _ in range(n):
        arr_item = int(fptr.readline())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.close()
    return result

print(testcase(1)==33556)