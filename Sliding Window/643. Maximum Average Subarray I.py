# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 
        count = 0
        while l<k:
            count+=nums[l]
            l+=1
        maxv = count/k
        while l<len(nums):
            count-=nums[l-k]
            count+=nums[l]
            i = count/k
            maxv = max(maxv,i)
            l+=1
        return maxv