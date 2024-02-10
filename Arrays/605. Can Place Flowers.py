# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            if n==1 and flowerbed[0]==0:
                return True
            elif n==0:
                return True
            return False
        for i in range(len(flowerbed)):
            if n==0:
                return True
            if i == 0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            elif i == len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                n-=1
            elif flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
        return n==0