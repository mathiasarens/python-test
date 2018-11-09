# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    root = buildTree(t_nodes, t_edges, t_from, t_to)
    
    # calculate children in subtree
    calculateChildrenInSubTree(root)

    # calculate edges to remove
    result = removeEdges(root)

    return result

def removeEdges(node):
    if not node.children:
        return 0 
    else:
        result = 0
        for child in node.children:
            result += removeEdges(child)
        if node.numberOfChildrenInSubTree % 2 == 0 and node.parent != None:
            result += 1
        return result



def calculateChildrenInSubTree(node):
    if not node.children:
        node.numberOfChildrenInSubTree = 1
        return 1
    result = 0
    for child in node.children:
        result += calculateChildrenInSubTree(child)
    result += 1
    node.numberOfChildrenInSubTree = result
    return result

def buildTree(t_nodes, t_edges, t_from, t_to):
    nodes = {}

    def getNode(index):
        if (nodes.get(index) == None):
            nodes[index] = TreeNode(index)
        return nodes[index]
    
    visited = {}
    queue = [1]
    while queue:
        node_value = queue.pop(0)
        for j in range(t_edges):
            if t_from[j] == node_value:
                if not visited.get(t_to[j], False):
                    getNode(node_value).addChild(getNode(t_to[j]))
                    getNode(t_to[j]).parent = getNode(node_value)
                    queue.append(t_to[j])

            if t_to[j] == node_value:
                if not visited.get(t_from[j], False):
                    getNode(node_value).addChild(getNode(t_from[j]))
                    getNode(t_from[j]).parent = getNode(node_value)
                    queue.append(t_from[j])
        visited[node_value] = True
    return nodes[1]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.parent = None
        self.children = []
        self.numberOfChildrenInSubTree = 0

    def addChild(self, node):
        self.children.append(node)


# print(evenForest(10, 9, [2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 1, 3, 2, 1, 2, 6, 8, 8]))
# print(evenForest(4, 3, [1,1,2],[2,3,4]))
# print(evenForest(6, 5, [1,1,1,1,1],[2,3,4,5,6]))
# print(evenForest(3, 2, [1,1],[2,3]))
# print(evenForest(10, 9, [2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 1, 3, 2, 1, 2, 6, 4, 8]))
# print(evenForest(10, 9, [2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 1, 3, 7, 1, 2, 6, 4, 8]))
# print(evenForest(4, 3, [1,1,8],[5,8, 10])==1)
print(evenForest(20, 19, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[1,1,3,2,5,1,1,2,7,10,3,7,8,12,6,6,10,1,8]) == 4)
# 2 1
# 3 1
# 4 3
# 5 2
# 6 5
# 7 1
# 8 1
# 9 2
# 10 7
# 11 10
# 12 3
# 13 7
# 14 8
# 15 12
# 16 6
# 17 6
# 18 10
# 19 1
# 20 8


# 10 9
# 2 1
# 3 1
# 4 3
# 5 2
# 6 1
# 7 2
# 8 6
# 9 8
# 10 8
