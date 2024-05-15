# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==1:
            return [str(nums[0])]
        l = 0
        r = len(nums)-1
        summary = []
        while l<r:
            ranges = [nums[l]]
            k = l
            i = l
            while l<r and nums[l]+1==nums[l+1]:
                l+=1
                k+=1
            if k!=i:
                summary.append(str(ranges[0])+'->'+str(nums[k]))
                l+=1
                if l==r:
                    summary.append(str(nums[l]))
                    l+=1
            else:
                summary.append(str(ranges[0]))
                l+=1
                if l==r:
                    summary.append(str(nums[l]))
                    l+=1
        return summary