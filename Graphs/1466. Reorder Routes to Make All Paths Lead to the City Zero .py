# 1466. Reorder Routes to Make All Paths Lead to the City Zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i,j in connections:
            graph[i].append((j,1))
            graph[j].append((i,0))
        
        visited = set()
        self.count = 0

        def dfs(city):
            if city in visited: return 0
            visited.add(city)
            
            for neighbor, direction in graph[city]:
                if neighbor not in visited:
                    self.count+=direction
                    dfs(neighbor)
            
        dfs(0)
        return self.count 