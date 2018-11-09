from collections import defaultdict


def minimumBribes(q):
    arr = q
    tooChotic = False
    numberOfBribesPerNode = defaultdict(lambda: 0)
    for i in range(len(arr)-1, 0,-1):
        if arr[i-1] == i+1:
            numberOfBribesPerNode[i+1] += 1
            arr[i-1] = arr[i]
        elif i >= 2 and arr[i-2] == i+1:
            numberOfBribesPerNode[i+1] += 2
            arr[i-2] = arr[i-1]
            arr[i-1] = arr[i]
        elif arr[i] != i+1:
            print("Too chaotic")
            tooChotic = True
            break
    if not tooChotic:
        numberOfBribes = 0
        for k,v in numberOfBribesPerNode.items():
            if v > 2:
                numberOfBribes = -1
                break
            else:
                numberOfBribes += v
        if numberOfBribes >= 0:
            print(numberOfBribes)
        else:
            print("Too chaotic")


minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])
minimumBribes([]) 
minimumBribes([1]) 
minimumBribes([1,2,3,4]) 
minimumBribes([1,2,4,3])
minimumBribes([1,4,2,3]) 
minimumBribes([4,1,2,3])
minimumBribes([1,44,2,3])
minimumBribes([5,1,2,3,7,8,6,4])
minimumBribes([1,2,5,3,7,8,6,4]) 
