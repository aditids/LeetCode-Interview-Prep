# 1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        count = 0
        while i<j:
            tsum = nums[i]+nums[j]
            if tsum==k:
                count+=1
                i+=1
                j-=1
            elif tsum<k:
                i+=1
            else:
                j-=1
        return count
        
        # kSumPairs = 0
        # count = Counter(nums)
        # for i in nums:
        #     j = k-i
        #     if count[i] and count[j]:
        #         if i==j:
        #             kSumPairs+=count[i]//2
        #             count[i]=0
        #         else:
        #             pairs = min(count[i],count[j])
        #             count[i]-=pairs
        #             count[j]-=pairs
        #             kSumPairs+=pairs
        # return kSumPairs