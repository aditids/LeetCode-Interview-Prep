# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clone = {}

        def dfs(node):
            if node in clone: 
                return clone[node]

            curr = Node(node.val)
            clone[node] = curr

            for i in node.neighbors:
                curr.neighbors.append(dfs(i))

            return curr

        return dfs(node)