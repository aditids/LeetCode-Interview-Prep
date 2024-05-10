# 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        count = 0

        def bfs(cur):
            q = [cur]
            while q:
                k = q.pop(0)
                for x in range(len(isConnected)):
                    if isConnected[k][x] == 1 and x not in visit:
                        visit.add(x)
                        q.append(x)

        for i in range(len(isConnected)):
            if i not in visit:
                count+=1
                visit.add(i)
                bfs(i)
        return count