# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        first, next = 1,1
        while n>1:
            n-=1
            temp = next
            next = first + next          
            first = temp
        return next          