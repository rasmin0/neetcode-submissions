# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre, inord):
            if not pre or not inord:
                return None

            root = TreeNode(pre[0])
            mid = inord.index(pre[0])

            root.left = build(pre[1:mid+1], inord[:mid])
            root.right = build(pre[mid+1:], inord[mid+1:])

            return root

        return build(preorder, inorder)


