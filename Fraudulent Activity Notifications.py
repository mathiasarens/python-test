def activityNotifications(expenditure, d):
    count = 0
    count_array = [0 for i in range(200+1)]
    expenditure_queue = []
    for i in range(d):
        expenditure_queue.append(expenditure[i])
        count_array[expenditure[i]]+=1

    for i in range(d, len(expenditure)):
        # Calculate Median
        median = calculate_median_of_count_array(count_array,d)
        if expenditure[i] >= 2 * median:
            count+=1
    
        # update count_array and expendiure_queue     
        # remove the oldest expenditure
        value_to_remove = expenditure_queue.pop(0)
        count_array[value_to_remove]-=1
        # insert current expenditure
        expenditure_queue.append(expenditure[i])
        count_array[expenditure[i]]+=1
    return count

def calculate_median_of_count_array(count_array, length_of_array):
    number_of_elements=0
    sum = 0
    for i in range(len(count_array)):
        number_of_elements += count_array[i]
        sum += count_array[i] * i
        if (2*number_of_elements) < length_of_array:
            continue
        elif (2*number_of_elements) == length_of_array:
            next = 0
            for j in range(i+1, len(count_array)):
                if count_array[j] > 0:
                    next = j 
                    break   
            return (i+next) / 2
        else:
            return i * 1.0


print(activityNotifications([1,2,3,4,4,7,1,1,2,3], 4)==2)
print(activityNotifications([1,2,3,4,4,7,1,1,2,2], 4)==1)

# Test for calculate_median_of_count_array
# array: 1234
print(calculate_median_of_count_array([0,1,1,1,1], 4) == 2.5)
# array: 1256
print(calculate_median_of_count_array([0,1,1,0,0,1,1], 4) == 3.5)
# array: 4589
print(calculate_median_of_count_array([0,0,0,0,1,1,0,0,1,1], 4) == 6.5)
# array 123
print(calculate_median_of_count_array([0,1,1,1], 3) == 2)
# array 234
print(calculate_median_of_count_array([0,0,1,1,1], 3) == 3)
# array 122223
print(calculate_median_of_count_array([0,1,4,1], 6) == 2)
# array 12223
print(calculate_median_of_count_array([0,1,3,1], 5) == 2)

if __name__ == '__main__':
    fptr = open('Fraudulent Activity Notifications-TestCase2.txt', 'r')
    nd = fptr.readline().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, fptr.readline().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(result==770)
    fptr.close()

def activityNotificationsSlowButCorrect(expenditure, d):
    count = 0
    
    for i in range(d, len(expenditure)):
        if i == d:
            median_array = expenditure[0:d]
            median_array.sort()
        else:
            median_array.remove(expenditure[i-d-1])
            for j in range(d-1):
                if expenditure[i-1]<median_array[j]:
                    median_array.insert(j, expenditure[i-1])
                    break
            if len(median_array) < d:
                median_array.append(expenditure[i-1])
        median = 0
        if d%2==0:
            median = (median_array[len(median_array)//2] + median_array[len(median_array)//2-1]) / 2
        else:
            median = median_array[len(median_array)//2]
        if expenditure[i] >= 2 * median:
            count+=1
    return count