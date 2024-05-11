# 1926. Nearest Exit from Entrance in Maze

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = [(entrance[0],entrance[1])]
        visit = set()
        visit.add((entrance[0],entrance[1]))
        steps = 0
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        while q:
            flag = 0
            for _ in range(len(q)):
                i,j = q.pop(0)
                for x,y in directions:
                    xi, yj = x+i, y+j
                    if xi<0 or yj<0 or xi>=len(maze) or yj>=len(maze[0]):
                        continue
                    elif maze[xi][yj]=='.' and (xi,yj) not in visit:
                        if xi == 0 or xi == len(maze) - 1 or yj == 0 or yj == len(maze[0]) - 1:
                            return steps + 1
                        q.append((xi,yj))
                        visit.add((xi,yj))
                    else:
                        flag+=1

            steps+=1
        return -1