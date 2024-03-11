# 399. Evaluate Division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjecencyList = defaultdict(list)
        for i, equation in enumerate(equations):
            ai, bi = equation
            adjecencyList[ai].append((bi,values[i]))
            adjecencyList[bi].append((ai,1/values[i]))

        def bfs(src,dest):
            if src not in adjecencyList or dest not in adjecencyList: return -1
            q = [[src,1]]
            visited = set()
            visited.add(src)
            while q:
                n, cur = q.pop(0)
                if n==dest:
                    return cur
                for neighbor, value in adjecencyList[n]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append([neighbor,cur*value])
                        
            return -1
        
        result = []
        for q in queries:
            result.append(bfs(q[0],q[1]))

        return result

        # Time complexity - O(N*Equations)
        # Space complexity = O(V+E)