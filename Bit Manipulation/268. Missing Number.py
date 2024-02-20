# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # total = n*(n+1)//2
        # return total-sum(nums)

        missing_number = len(nums)
        for i in range(len(nums)):
            missing_number+=i-nums[i]
            print(missing_number)
        return missing_number

# Time Complexity - O(n)
# Space Complexity - O(1)