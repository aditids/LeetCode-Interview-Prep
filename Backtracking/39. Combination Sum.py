# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def backtrack(i, curr, count):
            if count == target:
                combinations.append(curr.copy())
                return
            if i>=len(candidates) or count>target:
                return
            curr.append(candidates[i])
            backtrack(i, curr, count+candidates[i])
            curr.pop()
            backtrack(i+1, curr, count)
        backtrack(0,[],0)
        return combinations       