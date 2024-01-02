# 125. Valid Palindrome
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()
        lan = re.sub(r'[^a-z0-9]','',l)
        print(lan)
        i,j = 0, len(lan)-1
        while i<j:
            if lan[i]!=lan[j]:
                return False
            i+=1
            j-=1
        return True      
        # Time and Space Complexity - O(n)