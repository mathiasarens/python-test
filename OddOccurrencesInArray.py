def solution(A):
    number_occurances = {}
    for i in A:
        if i in number_occurances:
            number_occurances[i] += 1
        else:
            number_occurances[i] = 1
    for key, value in number_occurances.items():
        if (value % 2 == 1):
            return key
    return 0


print(solution([9,3,9,3,9,7,9]))
print(solution([2,2,2]))