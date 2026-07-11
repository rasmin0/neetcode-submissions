# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(root):
            nonlocal res, low, high
            if not root:
                return 0
            elif low < root.val and high < root.val:
                dfs(root.left)
            elif low > root.val and high > root.val:
                dfs(root.right)
            else:   
                res += root.val
                dfs(root.left)
                dfs(root.right)
            
            return res
        
        return dfs(root)