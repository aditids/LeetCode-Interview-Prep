# 224. Basic Calculator

class Solution:
    def calculate(self, s: str) -> int:

        def evaluate(stack):
            if not stack or type(stack[-1]) == str:
                stack.append(0)

            res = stack.pop()
            while stack and stack[-1]!=')':
                sign = stack.pop()
                if sign == '+':
                    res+=stack.pop()
                else:
                    res-=stack.pop()
            return res

        stack = []
        n = 0
        num = 0
        for i in range(len(s)-1,-1,-1):
            cur = s[i]
            if cur.isdigit():
                num = num + ((10**n)* int(cur))
                n+=1
            elif cur != ' ':
                if n:
                    stack.append(num)
                    num = 0
                    n = 0
                if cur == '(':
                    res = evaluate(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(cur)

        if n:
            stack.append(num)

        return evaluate(stack)