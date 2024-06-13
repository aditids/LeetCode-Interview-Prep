# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
        (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = ''
        for i,j in digits:
            if num == 0:
                break           
            k = num//i
            num = num%i
            res+=str(j*k)
        return res