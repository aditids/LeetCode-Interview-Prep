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
        clone = {}
        def dfs(node):
            if node in clone:
                return clone[node]
            currNode = Node(node.val)
            clone[node] = currNode
            for i in node.neighbors:
                currNode.neighbors.append(dfs(i))
            return currNode
        return dfs(node) if node else None
        