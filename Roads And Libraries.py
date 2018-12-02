def roadsAndLibraries(n, c_lib, c_road, cities):
    city_connection_map = create_city_connection_map(cities)
    visited_array = [False] * (n+1)
    min_costs = 0
    for i in range(1,n+1):
        if not visited_array[i]:
            roads = bfs(i, city_connection_map, visited_array)
            if roads >= 0:
                min_costs += min(roads*c_road+c_lib, (roads+1)*c_lib)
    return min_costs

def bfs(city, city_connection_map, visited_array):
    queue = []
    queue.append(city)
    roads = -1
    while queue:
        node = queue.pop(0)
        if not visited_array[node]:
            visited_array[node] = True
            roads+=1
            for dest_city in city_connection_map.get(node, []):
                queue.append(dest_city)
    return roads

def create_city_connection_map(cities):
    city_connection_map = {}
    for connection in cities:
        city_connection_map.setdefault(connection[0],[]).append(connection[1])
        city_connection_map.setdefault(connection[1],[]).append(connection[0])
    return city_connection_map


print(roadsAndLibraries(3, 2, 1, [(1,2),(3,1),(2,3)]) == 4)
print(roadsAndLibraries(6, 2, 5, [(1,3),(3,4),(2,4),(1,2),(2,3),(5,6)]) == 12)
print(roadsAndLibraries(1, 6, 6, []) == 6)
print(roadsAndLibraries(2, 6, 1, []) == 12)
print(roadsAndLibraries(2, 6, 1, [(1,2)]) == 7)