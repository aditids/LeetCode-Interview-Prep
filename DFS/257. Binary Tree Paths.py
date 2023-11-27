# 257. Binary Tree Paths
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        path = []
        def dfs(root):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:               
                paths.append("->".join(path))
                path.pop()
                return
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        return paths