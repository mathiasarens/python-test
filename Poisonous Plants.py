# Solution is wrong
# https://www.hackerrank.com/challenges/poisonous-plants/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues&h_r=next-challenge&h_v=zen
def poisonousPlants(p):
    killer_index_array = [None] * len(p)
    min_index_stack = []
    killer_index_array[0]= -1
    min_index_stack.append(0)
    max_days_array = [0] * len(p)
    max_days = 0
    for i in range(1,len(p)):
        if p[min_index_stack[0]] < p[i]:
            killer_index_array[i] = min_index_stack[0]
            max_days_array[killer_index_array[i]] += 1
            max_days = max(max_days, max_days_array[killer_index_array[i]])
        else:
            while len(min_index_stack)>1 and p[min_index_stack[0]] >= p[i]:
                min_index_stack.pop(0)
            if p[min_index_stack[0]] < p[i]:
                killer_index_array[i] = min_index_stack[0]
                max_days_array[killer_index_array[i]] += 1
                max_days = max(max_days, max_days_array[killer_index_array[i]])
            else:
                killer_index_array[i] = -1
        min_index_stack.insert(0,i)

    return max_days

print(poisonousPlants([4,3,7,5,6,4,2])==3)
print(poisonousPlants([4,5,3,2,1,6])==1)
print(poisonousPlants([20,5,6,15,2,2,17,2,11,5,14,5,10,9,19,12,5])==4)
print(poisonousPlants([20,5,6,15,2,2,17,2,11,5,14,5,10,9,19,12,5,1,0,10])==4)
print(poisonousPlants([4,3,9,7,8,6,7,5,2])==4)
print(poisonousPlants([4,3,9,7,8,2,7,5,1])==2)
print(poisonousPlants([3,1,10,7,3,5,6,6])==3)
print(poisonousPlants([3,6,2,7,5])==2)
print(poisonousPlants([6,5,8,4,7,10,9])==2)
print(poisonousPlants([6])==0)
print(poisonousPlants([6,5,4,3,2,1])==0)
print(poisonousPlants([6,7,8,9,10,11])==1)
print(poisonousPlants([6,7,8,7,8,9,8,9,10,9])==2)
print(poisonousPlants([6,7,8,7,8,9,8,9,10,9,8])==3)
print(poisonousPlants([0,0,0,0])==0)
print(poisonousPlants([0,1,1,1])==3)
print(poisonousPlants([0,1,1,0])==2)

def testcase(i, expected_result):
    fptr = open(f"Poisonous Plants-TestCase{i}.txt", 'r')
    n = int(fptr.readline())
    p = list(map(int, fptr.readline().rstrip().split()))
    result = poisonousPlants(p)
    if result == expected_result:
        print(True)
    else:
        print(f"{result} != {expected_result}")
    fptr.close()

# testcase(12, 16)