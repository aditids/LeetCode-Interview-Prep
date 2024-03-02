# 841. Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = [0]
        while q:
            r = q.pop(0)
            visited.add(r)
            for k in rooms[r]:
                if k not in visited:                    
                    q.append(k)
        return len(visited) == len(rooms)