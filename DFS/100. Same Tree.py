# 100. Same Tree
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q:
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return False

    #Time & Space Complexity: O(n)