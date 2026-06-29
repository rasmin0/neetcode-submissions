# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, val):
            nonlocal count
            if not root:
                return 0
            
            if root.val >= val:
                val = max(root.val, val)
                count += 1
            
            dfs(root.left, val)
            dfs(root.right, val)

            return count
        
        return dfs(root, root.val)