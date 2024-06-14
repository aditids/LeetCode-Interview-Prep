# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n = 0
        # for i in digits:
        #     n = n*10+i
        # n+=1
        # result = []
        # for i in str(n):
        #     result.append(int(i))
        # return result   

        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i]+=1
                return digits
        return [1]+digits