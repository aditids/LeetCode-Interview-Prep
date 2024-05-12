# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        hashtable = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}  

        def backtrack(path, cur):
            if cur == len(digits):
                combinations.append(''.join(path))
                return
            for i in hashtable[digits[cur]]:
                path.append(i)
                backtrack(path,cur+1)
                path.pop()

        backtrack([],0)
        return combinations