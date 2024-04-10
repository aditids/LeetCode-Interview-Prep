# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur,path):
            res.append(path)
            for i in range(cur,len(nums)):
                dfs(i+1,path+[nums[i]])

        dfs(0,[])
        return res