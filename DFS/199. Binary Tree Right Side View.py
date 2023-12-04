# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root, level):
            if not root:
                return
            if len(result)==level:
                result.append(root.val)
            print(result)
            
            dfs(root.right, level+1)            
            dfs(root.left, level+1)

            return result
        
        dfs(root, 0)
        return result
        