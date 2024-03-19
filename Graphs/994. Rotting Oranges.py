# 994. Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        count = 0
        fresh = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
                
        while q and fresh:
            n = len(q)
            for i in range(n):
                a,b = q.pop(0)
                for x,y in directions:
                    xi,yi = x+a, y+b
                    if xi>=0 and yi>=0 and xi<len(grid) and yi<len(grid[0]) and grid[xi][yi]==1:
                        grid[xi][yi] = 2
                        q.append((xi,yi))
                        fresh-=1
            if q:
                count+=1

        return -1 if fresh else count