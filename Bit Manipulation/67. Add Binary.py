# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        while len(a)<len(b):
            a = '0'+a
        while len(a)>len(b):
            b = '0'+b
        #print(a,b)
        for i in range(len(a)-1,-1,-1):
            temp = carry
            if a[i] == '1':
                temp+=1
            if b[i] == '1':
                temp+=1

            if temp%2 == 1:
                res = '1' + res
            else:
                res = '0' + res
            carry = temp//2
        if carry:
            res = '1' + res
        return res