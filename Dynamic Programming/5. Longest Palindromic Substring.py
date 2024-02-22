# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        def is_palindrome(i,j):
            start, end = 0,0
            while i>=0 and j<len(s) and s[i]==s[j]:
                start = i
                end = j
                i-=1
                j+=1
            return [start,end]

        for i in range(len(s)):
            odd = is_palindrome(i,i)
            even = is_palindrome(i,i+1)
            p = []
            if odd[1]-odd[0] > even[1]-even[0]:
                p = s[odd[0]:odd[1]+1]
            else:
                p = s[even[0]:even[1]+1]

            if len(p)>len(result):
                result = p
        
        return result