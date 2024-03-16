# 32. Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = [-1]
        maxcount = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:      
                    #print(i,stack[-1])              
                    maxcount = max(maxcount,i-stack[-1])
        return maxcount