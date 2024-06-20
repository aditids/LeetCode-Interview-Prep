# 149. Max Points on a Line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1

        for i in range(len(points)):
            hmap = defaultdict(int)
            p1 = points[i]
            for j in range(i+1,len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = inf
                else:
                    slope = (p1[1]-p2[1])/(p1[0]-p2[0])
                hmap[slope]+=1
                result = max(result, hmap[slope]+1)

        return result