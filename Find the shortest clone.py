import sys

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    color_count = 0
    start_node = 0
    for i in range(len(ids)):
        if ids[i] == val:
            color_count+=1
            start_node = ids[i]
    if color_count > 1:
        nodes_dict = create_nodes_dict(graph_from, graph_to)
        color_distance_list = bfs(start_node, nodes_dict, graph_nodes, ids, val)
        min_distance = sys.maxsize
        for i in range(1, len(color_distance_list)):
            min_distance = min(min_distance, color_distance_list[i]-color_distance_list[i-1])
        return min_distance
    else:
        return -1

def bfs(start_node, nodes_dict, graph_nodes, ids, val):
    visited_array = [False] * (graph_nodes+1)
    distance_array=[sys.maxsize] * (graph_nodes+1)
    distance_array[start_node] = 0
    queue = []
    queue.append(start_node)
    color_distance_list = []
    while queue:
        node = queue.pop(0)
        if not visited_array[node]:
            visited_array[node] = True
            if ids[node-1] == val:
                color_distance_list.append(distance_array[node])
            for dest_node in nodes_dict.get(node, []):
                distance_array[dest_node] = min(distance_array[dest_node], distance_array[node]+1)
                queue.append(dest_node)
    return color_distance_list

def create_nodes_dict(graph_from, graph_to):
    nodes_dict = {}
    for i in range(len(graph_from)):
        nodes_dict.setdefault(graph_from[i],[]).append(graph_to[i])
        nodes_dict.setdefault(graph_to[i],[]).append(graph_from[i])
    return nodes_dict


def testcase(i, expected_result):
    fptr = open(f"Find the shortest clone-TestCase{i}.txt", 'r')
    
    def input():
        return fptr.readline()

    graph_nodes, graph_edges = map(int, input().split())
    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges
    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())
    ids = list(map(int, input().rstrip().split()))
    val = int(input())
    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print(ans == expected_result)
    fptr.close()

testcase(0,1)
testcase(1,-1)
testcase(2,3)