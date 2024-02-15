# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        print(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        i,j = 0,len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            elif s[i] in vowels:
                j-=1
            elif s[j] in vowels:
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(s)
        