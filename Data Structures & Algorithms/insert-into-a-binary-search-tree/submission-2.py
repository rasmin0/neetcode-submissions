# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, num):
            if not node:
                return TreeNode(num)
            elif num < node.val:
                node.left = dfs(node.left, num)
            else:
                node.right = dfs(node.right, num)
            
            return node
        
        root = dfs(root, val)

        return root