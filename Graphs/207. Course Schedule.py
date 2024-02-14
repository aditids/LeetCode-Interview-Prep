# 207. Course Schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseList = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            courseList[course].append(prerequisite)

        visited = set()
        def dfs(course):
            if course in visited: return False
            if courseList[course] == []: return True

            visited.add(course)
            for i in courseList[course]:
                if not dfs(i): return False

            visited.remove(course)
            courseList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True

# Time and Space complexity = O(V+E)
# V = Number of Courses
# E = Number of Prerequisites