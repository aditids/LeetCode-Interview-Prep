# 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(root):
            while root!=parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root
        
        def union(r1,r2):
            p1,p2 = find(r1), find(r2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return 1

        visited = set()
        count = n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1 and (j,i) not in visited:
                    count -= union(i, j)
                    visited.add((i,j))
        return count