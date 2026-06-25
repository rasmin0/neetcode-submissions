# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = dfs(node.left, val)
            elif val > node.val:
                node.right = dfs(node.right, val)
            else:
                if not node.left and not node.right:
                    node = None
                elif node.left and not node.right:
                    node = node.left
                elif not node.left and node.right:
                    node = node.right
                else:
                    cur = node.right

                    while cur and cur.left:
                        cur = cur.left
                    
                    cur.val, node.val = node.val, cur.val

                    node.right = dfs(node.right, cur.val)
            return node
        
        root = dfs(root, key)

        return root