# 433. Minimum Genetic Mutation

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visit = set()
        q = [[startGene,0]]
        while q:
            cur, count = q.pop(0)
            if cur == endGene:
                return count
            for choice in 'ACGT':
                for i in range(8):
                    node = cur[:i] + choice + cur[i+1:]
                    if node not in visit and node in bank:
                        q.append([node, count+1])
                        visit.add(node)
        return -1