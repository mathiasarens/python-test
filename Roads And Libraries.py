def roadsAndLibraries(n, c_lib, c_road, cities):
    city_connection_map = create_city_connection_map(cities)
    visited_array = [False] * (n+1)
    min_costs = 0
    for i in range(1,n+1):
        if not visited_array[i]:
            roads = dfs(i, city_connection_map, visited_array,-1)
            if roads >= 0:
                min_costs += min(roads*c_road+c_lib, (roads+1)*c_lib)
    return min_costs

def dfs(city, city_connection_map, visited_array, roads):
    if not visited_array[city]:
        visited_array[city] = True
        roads+=1
        for k,v in city_connection_map.items():
            if k == city:
                roads = max(roads, dfs(v, city_connection_map, visited_array, roads))
            if v == city:
                roads = max(roads, dfs(k, city_connection_map, visited_array, roads))
    return roads

def create_city_connection_map(cities):
    city_connection_map = {}
    for connection in cities:
        city_connection_map.setdefault(connection[0],connection[1])
        city_connection_map.setdefault(connection[1],connection[0])
    return city_connection_map


print(roadsAndLibraries(3, 2, 1, [(1,2),(3,1),(2,3)]) == 4)
print(roadsAndLibraries(6, 2, 5, [(1,3),(3,4),(2,4),(1,2),(2,3),(5,6)]) == 12)
print(roadsAndLibraries(1, 6, 6, []) == 6)
print(roadsAndLibraries(2, 6, 1, []) == 12)
print(roadsAndLibraries(2, 6, 1, [(1,2)]) == 7)