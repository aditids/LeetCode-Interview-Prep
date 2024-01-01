# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     if target-nums[i] in nums and nums.index(target-nums[i])!=i:
        #         result.append(i)
        #         result.append(nums.index(target-nums[i]))
        #         return result
        # Time complexity  - O(n^2) and Space Complexity - O(1)

        # Using Hash table - 

        hasht = {}
        for i,a in enumerate(nums):
            b = target - a
            if b in hasht:
                return [i, hasht[b]]
            hasht[a] = i
        return []
        # Time complexity  - O(n)
        # Space Complexity - O(1)