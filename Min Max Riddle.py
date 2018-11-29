# Complete the riddle function below.
def riddle(arr):
    min_stack=[]
    min_next = [0]*len(arr)
    for i in range(len(arr)):
        while min_stack and min_stack[0][0] > arr[i]:
            value, index = min_stack.pop(0)
            min_next[index] = i
        min_stack.insert(0, (arr[i],i))
    while min_stack:
        value, index = min_stack.pop(0)
        min_next[index] = len(arr)

    min_prev = [0] * len(arr)
    for i in range(len(arr)-1,-1,-1):
        while min_stack and min_stack[0][0] > arr[i]:
            value, index = min_stack.pop(0)
            min_prev[index] = i
        min_stack.insert(0, (arr[i],i))
    while min_stack:
        value, index = min_stack.pop(0)
        min_prev[index] = -1

    result = [0] * (len(arr)+1)
    for i in range(len(arr)):
        size = min_next[i]-min_prev[i]-1
        result[size] = max(result[size], arr[i])
    for i in range(len(result)-2,0,-1):
        result[i] = max(result[i],result[i+1])
    return result[1:]

print(riddle([10,20,30,50,10,70,30])==[70,30,20,10,10,10,10])
print(riddle([6,3,5,1,12])==[12,3,3,1,1])
print(riddle([2,6,1,12])==[12,2,1,1])
print(riddle([1,2,3,5,1,13,3])==[13,3,2,1,1,1,1])
print(riddle([3,5,4,7,6,2])==[7,6,4,4,3,2])
print(riddle([])==[])
print(riddle([4])==[4])
print(riddle([4,4])==[4,4])
print(riddle([4,5])==[5,4])
print(riddle([5,4])==[5,4])
print(riddle([5,4,3,2,1])==[5,4,3,2,1])


def testcase(i):
    fptr_testcase = open(f"Min Max Riddle-TestCase{i}.txt", 'r')
    fptr_solution = open(f"Min Max Riddle-Solution{i}.txt", 'r')

    n = int(fptr_testcase.readline())

    arr = list(map(int, fptr_testcase.readline().rstrip().split()))

    res = riddle(arr)
    expected_solution_list = list(map(int, fptr_solution.readline().rstrip().split()))
    
    if len(res) == len(expected_solution_list):
        for i in range(len(res)):
            if res[i] != expected_solution_list[i]:
                print(f"{i}: {res[i]} != {expected_solution_list[i]}")
    else:
        print(f"List have not the same size: {len(res)} {len(expected_solution_list)}")
    
    fptr_testcase.close()
    fptr_solution.close()

testcase(2)
        
    