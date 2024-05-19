# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for char in magazine:
            if char in letters:
                letters[char]+=1
            else:
                letters[char] = 1
        for char in ransomNote:
            if char in letters and letters[char]>0:
                letters[char]-=1
            else:
                return False
        return True