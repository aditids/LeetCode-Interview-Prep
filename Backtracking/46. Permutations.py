# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums)==1:
            return [nums[:]]
        def dfs(path, visited):
            if len(path)==len(nums):
                res.append(path[:])
                return 
            for i in nums:
                if i not in visited:
                    path.append(i)
                    visited.add(i)
                    dfs(path,visited)
                    path.pop()
                    visited.remove(i)       
        dfs([],set())
        return res