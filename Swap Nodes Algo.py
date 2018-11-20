def swapNodes(indexes, queries):
    result = []
    for k in queries:
        swap(indexes, 1, 1, k)
        result.append(level_order(indexes, 1))
    return result


def swap(indexes, node, current_level, k):
    if indexes[node-1][0] != -1:
        swap(indexes, indexes[node-1][0], current_level+1, k)
    if indexes[node-1][1] != -1:
        swap(indexes, indexes[node-1][1], current_level+1, k)
    if current_level % k == 0:
        temp = indexes[node-1][0]
        indexes[node-1][0] = indexes[node-1][1]
        indexes[node-1][1] = temp


def level_order(indexes, node):
    res = []
    if indexes[node-1][0] != -1:
        res.extend(level_order(indexes, indexes[node-1][0]))
    res.append(node)
    if indexes[node-1][1] != -1:
        res.extend(level_order(indexes, indexes[node-1][1]))
    return res


print(swapNodes([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1],
                 [-1, -1]], [2, 4]) == [[2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10], [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]])
print(swapNodes([[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1],
                 [-1, -1], [-1, -1]], [2, 3]) == [[14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16], [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15]])
print(swapNodes([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]], [2, 4]) == [[2,9,6,4,1,3,7,5,11,8,10],[2,6,9,4,1,3,7,5,10,8,11]])


