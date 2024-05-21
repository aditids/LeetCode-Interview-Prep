# 22. Generate Parentheses

class Solution:
    def __init__(self):
        self.combinations = [] 

    def generateParenthesis(self, n: int) -> List[str]:
        
        self.backtrack([],0,0, n)
        return self.combinations

    def backtrack(self, cur, left, right, n):
        if len(cur) == 2*n:
            self.combinations.append(''.join(cur))
            return
        if left<n:
            cur.append('(')
            self.backtrack(cur, left+1, right, n)
            cur.pop()
        if right<left:
            cur.append(')')
            self.backtrack(cur, left, right+1, n)
            cur.pop()