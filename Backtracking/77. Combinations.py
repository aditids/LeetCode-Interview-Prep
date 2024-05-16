# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(i, k_cur, combination):
            if k_cur == k:
                result.append(combination.copy())
                return
            for j in range(i,n+1):
                combination.append(j)
                backtrack(j+1,k_cur+1, combination)
                combination.pop()

        backtrack(1,0,[])
        return result