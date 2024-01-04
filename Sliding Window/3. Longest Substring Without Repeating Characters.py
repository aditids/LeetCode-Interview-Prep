# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # count = 0
        # for i in range(len(s)):
        #     result = []
        #     k = i
        #     while k<len(s) and s[k] not in result:
        #         result.append(s[k])
        #         k+=1
        #     count = max(count,len(result))
        # return count

        substr = set()
        i = 0
        count = 0
        for j in range(len(s)):
            while s[j] in substr:
                substr.remove(s[i])
                i+=1
            substr.add(s[j])
            count = max(count, j-i+1)
        return count