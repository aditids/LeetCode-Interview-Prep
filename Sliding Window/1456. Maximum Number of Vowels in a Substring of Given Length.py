# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        l = 0
        count = 0
        while l<k:
            if s[l] in vowels:
                count+=1
            l+=1
        maxcount = count
        while l<len(s):
            if s[l-k] in vowels:
                count-=1
            if s[l] in vowels:
                count+=1
            maxcount = max(maxcount,count)
            l+=1
        return maxcount