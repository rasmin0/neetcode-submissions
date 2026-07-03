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
            nonlocal low, high, res
            if not root:
                return 0
            elif low > root.val:
                dfs(root.right)
            elif high < root.val:
                dfs(root.left)
            else:
                res += root.val
                dfs(root.left)
                dfs(root.right)
            
            return res
        
        return dfs(root)
