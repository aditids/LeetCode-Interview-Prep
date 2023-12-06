# 863. All Nodes Distance K in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        result = []

        def dfs(node, parent):
            if node and parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                dfs(node.left,node)
            if node.right:
                dfs(node.right,node)
        
        dfs(root, None)
        q = deque([(target.val,0)])
        visited.add((target.val))
        while q:
            curr, distance = q.popleft()
            if distance == k:
                result.append(curr)
            for i in graph[curr]:
                if i not in visited:
                    visited.add(i)
                    q.append((i,distance+1))

        return result

# Time and Space Complexity - O(n)