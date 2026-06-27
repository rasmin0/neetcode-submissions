# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        def dfs(root):
            nonlocal maxLen
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right
            maxLen = max(maxLen, diameter)
            return 1 + max(left, right)
        
        dfs(root)
        
        return maxLen
