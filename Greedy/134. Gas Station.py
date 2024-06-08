# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        total = 0
        res = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total+=gain
            cur+=gain
            if cur<0:
                cur = 0
                res = i+1
        return res if total>=0 else -1