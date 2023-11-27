# 112. Path Sum
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, tsum):
        if not root:
            return False
        tsum+=root.val
        if not root.right and not root.left:
            return tsum == targetSum          
        return dfs(root.left,tsum) or dfs(root.right,tsum)
            
    return dfs(root,0)        
    #Time & Space Complexity: O(n)