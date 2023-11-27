# 543. Diameter of Binary Tree
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.d = 0
    def dfs(root):
        if not root: return 0
        l = dfs(root.left)
        r = dfs(root.right)
        self.d = max(self.d, l+r)
        return max(l,r)+1
    dfs(root)
    return self.d
    # Time complexity = O(n)
    # Space complexity = O(n)