# 104. Maximum Depth of Binary Tree
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return 1+max(right, left)
    # Time complexity = O(n)
    # Space complexity = O(n)