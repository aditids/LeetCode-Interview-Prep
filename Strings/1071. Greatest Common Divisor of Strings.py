# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        def checkDivisor(i):
            if m%i == 0 and n%i == 0:
                a = m//i
                b = n//i
                if str1[:i]*a == str1 and str1[:i]*b == str2:
                    return True
            return False

        for i in range(min(m,n),0,-1):
            if checkDivisor(i):
                return str1[:i]
        return "" 

# Time Complexity - O(min(m,n)*(n+m))      