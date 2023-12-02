# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            prereq[course].append(pre)

        def dfs(course):
            if course in visited: return False
            if prereq[course] == []: return True

            visited.add(course)
            for i in prereq[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            prereq[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

# Time and Space complexity = O(V+E)
# V = Number of Courses
# E = Number of Prerequisites