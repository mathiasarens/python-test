# Complete the almostSorted function below.
def almostSorted(arr):
    swap_index_start = -1
    swap_index_end = -1
    i = 0
    j = len(arr)-1
    while(i<j and (swap_index_start<0 or swap_index_end <0)): 
        if arr[i] > arr[i+1]:
            swap_index_start=i
        if arr[j-1]>arr[j]:
            swap_index_end=j
          
        if swap_index_start < 0:
            i+=1
        if swap_index_end < 0:
            j-=1
            
    if i>=j:
        print("yes")
    else:
        decreasing_length = 0
        for k in range(swap_index_start+1,swap_index_end):
                if arr[k] > arr[k+1]:
                    decreasing_length+=1
        increasing_length = 0
        for k in range(swap_index_start,swap_index_end):
                if arr[k] < arr[k+1]:
                    increasing_length+=1
        # check if after swap or reverse if the 
        if (swap_index_end<len(arr)-1 and arr[swap_index_start] > arr[swap_index_end+1]) or (swap_index_start>0 and arr[swap_index_start-1] > arr[swap_index_end]):
            print("no")
        else:
            if j-1-i == decreasing_length and decreasing_length > 1:
                print("yes")
                print("reverse", i+1, j+1)
            elif j-1-i == decreasing_length and decreasing_length <=1 or j-2-i == increasing_length:    
                print("yes")
                print("swap", i+1, j+1)  
            else:
                print("no")  
         

#almostSorted([1,2]) # yes
#almostSorted([1,2,3,4,5,6,7]) # yes
#almostSorted([1,2,3,4,5,6,7,7]) # yes
#almostSorted([4,2]) # swap 1 2
#almostSorted([3,1,2]) # no
#almostSorted([1,5,4,3,2,6]) # reverse 2 5
#almostSorted([1,4,3,2,6]) # swap 2 4
#almostSorted([1,5,3,4,2,6]) # swap 2 5
#almostSorted([6,5,4,3,2,1]) # reverse 1 6
#almostSorted([6,2,3,4,5,1]) # swap 1 6
almostSorted([1,5,2,3,4,6]) # Swap start, kein Ende