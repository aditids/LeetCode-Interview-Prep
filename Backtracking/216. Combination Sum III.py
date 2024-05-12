# 216. Combination Sum III

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        def backtrack(path, cur, n):
            if n<0:
                return
            if n==0 and len(path)==k:
                combinations.append(path.copy()) 
                return
            for i in range(cur,10):
                path.append(i)
                backtrack(path,i+1,n-i)
                path.pop()
        backtrack([],1, n)
        return combinations