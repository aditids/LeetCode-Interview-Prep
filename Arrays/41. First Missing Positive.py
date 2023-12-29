# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)        
        
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                continue
            
            temp = nums[i]
            while nums[temp-1]!=temp:
                nums[temp-1], temp = temp, nums[temp-1]
                if temp<=0 or temp>n:
                    break
                
        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        return n+1      

        # Time Complexity - O(n)
        # Space Complexity - O(1)