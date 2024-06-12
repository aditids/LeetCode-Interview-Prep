# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = defaultdict(list)
        for i,j in prerequisites:
            course[i].append(j)
        
        visit = set()
        cycle = set()
        result = []
        
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True

            cycle.add(i)
            for k in course[i]:
                if not dfs(k):
                    return False
            
            cycle.remove(i)
            visit.add(i)
            result.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result