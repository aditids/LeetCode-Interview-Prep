# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i, subset):
            res.add(tuple(sorted(subset)))
            for j in range(i,len(nums)):
                dfs(j+1,subset+[nums[j]])
            
        dfs(0,[])
        return [list(x) for x in res]