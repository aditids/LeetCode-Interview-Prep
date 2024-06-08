# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000} 
        romans = {'I':['V','X'],'X':['L','C'],'C':['D','M']}
        result = 0
        i = len(s)-1
        while i>=0:
            if i>0 and s[i-1] in romans and s[i] in romans[s[i-1]] and s[i]!=s[i-1]:
                result+=dictionary[s[i]]-dictionary[s[i-1]]               
                i-=2

            else:
                result+=dictionary[s[i]]
                i-=1
            #print(result)
        return result