# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[]for i in range(numCourses)}
        visited = set()
        cycle = set()
        output = []
        for course, preq in prerequisites:
            prereq[course].append(preq)
        def dfs(course):
            if course in cycle: return False
            if course in visited: return True

            cycle.add(course)
            for preq in prereq[course]:
                if not dfs(preq): return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return output

# Time and Space complexity = O(V+E)
# V = Number of Courses
# E = Number of Prerequisites