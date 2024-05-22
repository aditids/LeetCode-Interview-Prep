# 274. H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for i, citation in enumerate(citations):
            if citation>=i+1:
                res = i+1
                continue
            break
        return res