def solution(A):
    numbersDict = {}
    for number in A:
        numbersDict[number] = 1

    for i in range(1,len(A)+2):
        if i not in numbersDict:
            return i
    return -1


print(solution([]))