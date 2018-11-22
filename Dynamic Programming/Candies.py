def candies(n, arr):
    candies_sum = 1
    last_drop_index = -1
    last_candy_amount = 1
    for i in range(1,len(arr)):
        # 3 2 3 / 2 2 2
        if arr[i-1] >= arr[i] and i < len(arr)-1 and arr[i+1] >= arr[i]:
            last_candy_amount = 1
            candies_sum+=last_candy_amount
        # 3 2 1 
        elif arr[i-1] > arr[i] and i < len(arr)-1 and arr[i+1] < arr[i]:
            if last_candy_amount > 1:
                last_candy_amount-=1
                candies_sum+=last_candy_amount
            else:
                candies_sum+=i-last_peak_index+1
        # 6 3 / 6 6
        elif arr[i-1] >= arr[i]:
            last_candy_amount = 1
            candies_sum+=last_candy_amount
        # 1 2 2 / 1 2 3 / 1 2 1 / 2 3
        elif arr[i-1] < arr[i]:
            last_candy_amount+=1
            last_peak_index = i
            candies_sum+=last_candy_amount
    return candies_sum
        


# print(candies(3, [1, 2, 2]) == 4)
print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
# print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]) == 19)
# print(candies(8, [2, 4, 3, 5, 2, 6, 4, 5]) == 12)

# print(candies(8, [8,7,6,5,4,5,6,7,2,1]) == 12)