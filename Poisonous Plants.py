# Solution is wrong
# https://www.hackerrank.com/challenges/poisonous-plants/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues&h_r=next-challenge&h_v=zen
def poisonousPlants(p):
    global_min_value = p[0]
    max_day_count = 0
    current_day_counter = 0
    above_global_minimum = False
    last_minimum = -1
    last_minimum_counter = -1
    for i in range(1,len(p)):
        if p[i-1] < p[i]:
            above_global_minimum = True
            current_day_counter=1
            max_day_count = max(max_day_count, current_day_counter)
        elif above_global_minimum and p[i-1] >= p[i] and p[i] > global_min_value:
            if p[i] > last_minimum:
                current_day_counter+=1
            if p[i] <= last_minimum:
                last_minimum_counter+=1
                current_day_counter=last_minimum_counter
            max_day_count = max(max_day_count, current_day_counter)
            last_minimum = p[i]
            last_minimum_counter = current_day_counter
        elif above_global_minimum and p[i-1] >= p[i] and p[i] < global_min_value:
            above_global_minimum = False
            global_min_value = p[i]
            max_day_count = max(max_day_count, current_day_counter)
            last_minimum = p[i]
            last_minimum_counter = -1
        elif above_global_minimum and p[i-1] >= p[i] and p[i] == global_min_value:
            above_global_minimum = False
            current_day_counter = 0
        elif p[i] < global_min_value:
            global_min_value = p[i]
            last_minimum = p[i]
    max_day_count = max(max_day_count, current_day_counter)
    return max_day_count

# 20 5 2 2 2 5 5 9 12 5
# 20 5 2 2 2 5 5
# 20 5 2 2 2 5
# 20 5 2 2 2 
print(poisonousPlants([20,5,6,15,2,2,17,2,11,5,14,5,10,9,19,12,5])==4)
print(poisonousPlants([4,5,3,2,1,6])==1)
print(poisonousPlants([4,3,7,5,6,4,2])==3)
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