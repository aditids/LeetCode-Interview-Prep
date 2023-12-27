# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0
        reduced = set(nums)
        for i in nums:
            count = 0
            if i-1 not in reduced:
                k = i
                while k in reduced:
                    k+=1
                    count+=1
                maxcount = max(maxcount, count)

        return maxcount

# Time and Space Complexity - O(n)