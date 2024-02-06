# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i<0 and stack[-1]>0:                
                if abs(stack[-1])>abs(i):
                    i = 0
                elif abs(stack[-1])<abs(i):
                    stack.pop()                    
                else:
                    i = 0
                    stack.pop()
            if i:
                stack.append(i)
        return stack
# Time and Space Complexity - O(n)