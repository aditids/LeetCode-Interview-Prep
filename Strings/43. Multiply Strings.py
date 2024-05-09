# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        dt = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        n1 = n2 = 0
        
        for i in num1:
            n1 = n1*10+dt[i]

        for i in num2:
            n2 = n2*10+dt[i]
            
        return str(n1*n2)