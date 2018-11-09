def organizingContainers(container):
    if len(container) < 1:
        return "Impossible"
    elif len(container[0])<1:
        return "Impossible"
    else:
        verticalSums = [0] * len(container)
        horizontalSums = [0] * len(container)
        for i in range(len(container)):
            for j in range(len(container)):
                horizontalSums[i] += container[i][j]
        for i in range(len(container)):
            for j in range(len(container)):
                verticalSums[i] += container[j][i]
        if sorted(horizontalSums) == sorted(verticalSums):
            return "Possible"
        else:
            return "Impossible"


print(organizingContainers([]))
print(organizingContainers([[]]))
print(organizingContainers([[1]]))
print(organizingContainers([[0,2],[1,1]]))
print(organizingContainers([[7, 0, 0], [0, 0, 9], [0, 3, 0]]))
print(organizingContainers([[6, 1, 0], [0, 0, 9], [1, 2, 0]]))
print(organizingContainers([[5, 1, 1], [1, 1, 7], [1, 1, 1]]))

# 7 0 0
# 0 0 9
# 0 3 0

# 6 1 0   6 1 0
# 0 0 9   0 1 8
# 1 2 0   1 2 0

# 5 1 1
# 1 0 8
# 1 2 0

# 5 1 1
# 1 1 7
# 1 1 1


# 4 1 1
# 2 1 7
# 1 1 1

# 1 1 0   2 0 0
# 1 1 1   0 3 0
# 0 1 2   0 0 3

# 1 1
# 1 1


