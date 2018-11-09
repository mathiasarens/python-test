import sys
def knightlOnAChessboard(n):
    result_matrix = [[-1 for i in range(n-1)] for i in range(n-1)]
    for i in range(0,n-1):
        for j in range(0,n-1):
            shortest_path = dijkstra(n, i+1, j+1)
            result_matrix[i][j] = shortest_path
            result_matrix[j][i] = shortest_path
    return result_matrix

def dijkstra(n, a, b):
    costs = [[-1 for i in range(n)] for i in range(n)]
    visited = [[False for i in range(n)] for i in range(n)]
    queue = []
    queue.append((0,0))
    costs[0][0]=0
    while queue:
        node = queue.pop(0)
        if not visited[node[0]][node[1]]:
            visited[node[0]][node[1]] = True
            # generate next nodes
            next_nodes_list = [(node[0]+a, node[1]+b),(node[0]+a, node[1]-b),(node[0]-a, node[1]+b),(node[0]-a, node[1]-b),(node[0]+b, node[1]+a),(node[0]+b, node[1]-a),(node[0]-b, node[1]+a),(node[0]-b, node[1]-a)]
            # filter valid nodes
            next_nodes_set = set(filter(lambda node: 0<=node[0]<n and 0<=node[1]<n, next_nodes_list))
            # add next nodes to queue
            queue.extend(next_nodes_set)

            # calculate shortest path
            min_costs = sys.maxsize
            for (x,y) in next_nodes_set:
                if visited[x][y]:
                    min_costs = min(min_costs, costs[x][y]+1)
            if min_costs < sys.maxsize:
                costs[node[0]][node[1]] = min_costs
    return costs[n-1][n-1]

n = 5
result_matrix = knightlOnAChessboard(n)
for i in range(n-1):        
    print(' '.join(map(lambda x: str(x), result_matrix[i])))
            

    