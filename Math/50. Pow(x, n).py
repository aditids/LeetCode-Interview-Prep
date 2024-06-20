# 50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x**n

        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        
        result = 1
        while n:
            if n%2 != 0:
                result*=x
                n-=1
            n = n/2
            x = x*x
        return result
    
    # Time complexity - O(logn)