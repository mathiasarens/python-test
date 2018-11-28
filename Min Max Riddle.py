# Complete the riddle function below.
def riddle(arr):
    queues_array=[]
    result = []
    for i in range(len(arr)):
        queues_array.append([[arr[i]], arr[i]])
        
    while len(queues_array) > 1:
        maximum = 0
        for i in range(len(queues_array)):
            maximum = max(maximum, queues_array[i][1])
            if i < len(queues_array)-1:
                element_from_next_queue = queues_array[i+1][0][-1]
                if element_from_next_queue < queues_array[i][1]:
                    queues_array[i][1] = element_from_next_queue
                queues_array[i][0].append(element_from_next_queue)
        del queues_array[-1]
        result.append(maximum)
    if len(queues_array) > 0:
        result.append(queues_array[0][1])
    return result

# print(riddle([6,3,5,1,12])==[12,3,3,1,1])
# print(riddle([2,6,1,12])==[12,2,1,1])
# print(riddle([1,2,3,5,1,13,3])==[13,3,2,1,1,1,1])
# print(riddle([3,5,4,7,6,2])==[7,6,4,4,3,2])
# print(riddle([])==[])
# print(riddle([4])==[4])
# print(riddle([4,4])==[4,4])
# print(riddle([4,5])==[5,4])
# print(riddle([5,4])==[5,4])
# print(riddle([5,4,3,2,1])==[5,4,3,2,1])


def testcase(i):
    fptr_testcase = open(f"Min Max Riddle-TestCase{i}.txt", 'r')
    fptr_solution = open(f"Min Max Riddle-Solution{i}.txt", 'r')

    n = int(fptr_testcase.readline())

    arr = list(map(int, fptr_testcase.readline().rstrip().split()))

    res = riddle(arr)
    expected_solution = fptr_solution.readline()
    
    print(' '.join(map(str, res)) == expected_solution)

    fptr_testcase.close()
    fptr_solution.close()

testcase(2)
        
    