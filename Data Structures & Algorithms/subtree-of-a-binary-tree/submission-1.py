# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            if node.val != sub.val:
                return False
            return dfs(node.left, sub.left) and dfs(node.right, sub.right)
        
        def same(root):
            nonlocal subRoot
            if not root:
                return False
            if dfs(root, subRoot):
                return True

            return same(root.left) or same(root.right)

        return same(root)