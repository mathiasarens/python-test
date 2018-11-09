import queue
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited_rooms = [None] * len(rooms)
        rooms_queue = queue.Queue()
        for i in range(len(rooms[0])):
            rooms_queue.put(rooms[0][i])
        visited_rooms[0] = True
        while rooms_queue.empty() is False:
            key = rooms_queue.get()
            if visited_rooms[key] is None:
                visited_rooms[key] = True
                for i in range(len(rooms[key])):
                    rooms_queue.put(rooms[key][i])

        return None not in visited_rooms

solution = Solution()
print(solution.canVisitAllRooms([[1],[2],[3],[]])) # => True
print(solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) #=> False
print(solution.canVisitAllRooms([[1],[2],[],[3]])) #=> False