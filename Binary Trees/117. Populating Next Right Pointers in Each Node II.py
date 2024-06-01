# 117. Populating Next Right Pointers in Each Node II

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q = [root]
        stack = []
        while q:
            n = len(q)
            for i in range(len(q)):
                cur = q.pop(0)
                if i<n-1:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
        return root