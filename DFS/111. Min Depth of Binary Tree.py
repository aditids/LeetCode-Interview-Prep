# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        def bfs():
            if not root: 
                return 0
            queue = [root]
            minBfs = 0
            while queue:
                n = len(queue)
                minBfs+=1
                for i in range(n):
                    tempNode = queue.pop(0)
                    if not tempNode.left and not tempNode.right:
                        return minBfs
                    if tempNode.left:
                        queue.append(tempNode.left)
                    if tempNode.right:
                        queue.append(tempNode.right)
            return minBfs
        
        # Time Complexity: O(n) -> number of nodes in tree
        # Space Complexity: O(h) -> height of tree
        def dfs(root):
            if not root:
                return 0
            if not root.left:
                return dfs(root.right)+1
            if not root.right:
                return dfs(root.left)+1
            if root.left and root.right:
                return min(dfs(root.left),dfs(root.right))+1

        minBfs = bfs()
        minDfs = dfs(root)

        return minBfs
        #return minDfs