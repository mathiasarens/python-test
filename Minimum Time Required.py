import math
# Complete the minTime function below.
def minTime(machines, goal):
    min_day = math.ceil(goal/len(machines)) * min(machines)
    max_day = math.ceil(goal/len(machines)) * max(machines)
    while min_day < max_day:
        tmp = (max_day + min_day) // 2
        if sum(tmp // m for m in machines) >= goal:
            max_day = tmp
        else:
            min_day = tmp +1
    return min_day

print(minTime([2,3], 5)==6)
print(minTime([1,8,9], 5)==5)
print(minTime([1,3,4], 10)==7)
print(minTime([4,5,6], 12)==20)
print(minTime([1,5,6], 5)==5)
print(minTime([1,5,6], 6)==5)
print(minTime([1,5,6], 7)==6)
print(minTime([1,2,5,6], 5)==4)
print(minTime([1,2,5,6], 6)==4)
print(minTime([1,2,15,16], 16)==11)
print(minTime([63,2,26,59,16,55,99,21,98,65], 56)==82)

def minTimeSearchBestSolutionFromLeaderBoard(machines, goal):
    minday = math.ceil(goal / len(machines)) * min(machines)
    maxday = math.ceil(goal / len(machines)) * max(machines)
    while minday < maxday:
        day = (maxday + minday) // 2
        if sum(day // m for m in machines) >= goal:
            maxday = day
        else:
            minday = day + 1
    return minday

def minTimeNaive(machines, goal):
    count = 0
    days = 1
    while count < goal:
        for machine in machines:
            if days%machine == 0:
                count+=1
        days += 1
    return days-1
    
# print(minTimeNaive([1,5,6],6))
# print(minTimeNaive([63,2,26,59,16,55,99,21,98,65], 56)==82)


def minTimeIncorrect(machines, goal):
    machines.sort()
    count = 0
    days = 0
    last_machine = 0
    while count < goal:
        i = 0
        while i < len(machines) and count < goal:
            if i > 0:
                for j in range(i):
                    count+=(machines[i]-machines[i-1])//machines[j]
                
            count+=1
            days+=abs(machines[i]-last_machine)
            if last_machine > 0 and i == 0:
                count+=abs(machines[i]-last_machine)//machines[i]
            last_machine=machines[i]
            i+=1
    return days

def minTimeCorrectButStillToSlow(machines, goal):
    machines.sort()
    count = 0
    days = 0
    free_machine_pool=machines
    used_machine_pool=[]
    while count < goal or used_machine_pool:
        while len(free_machine_pool) > 0 and count < goal:
            machine = free_machine_pool.pop(0)
            if not other_machine_that_is_faster(used_machine_pool, machine, goal - count):
                insert_pos = bisect.bisect_left([r[1] for r in used_machine_pool], machine)
                used_machine_pool.insert(insert_pos, [machine, machine])
                count+=1
        if used_machine_pool:
            (machine, rest_days) = used_machine_pool.pop(0)
            for i in range(len(used_machine_pool)):
                used_machine_pool[i][1]-=rest_days
            free_machine_pool.append(machine)
            days+=rest_days
    return days

def other_machine_that_is_faster(used_machine_pool, machine, count_diff):
    through_put = 0
    for used_machine in used_machine_pool:
        through_put += (machine-used_machine[1])//used_machine[0]
    return through_put >= count_diff

# print(minTimeCorrectButStillToSlow([1,2,15,16], 16)==11)
# print(minTimeCorrectButStillToSlow([63,2,26,59,16,55,99,21,98,65], 56)==82)

