# 443. String Compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r = 0,0
        while r<len(chars):
            count = 0
            cur = chars[r]
            while r<len(chars) and cur==chars[r]:
                count+=1
                r+=1
            chars[l] = cur
            l+=1
            if count>1:
                for i in str(count):
                    chars[l] = i
                    l+=1
        return l