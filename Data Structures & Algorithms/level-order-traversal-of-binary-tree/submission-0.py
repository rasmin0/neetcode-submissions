# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        arr = []

        if root:
            queue.append(root)
        

        while len(queue) > 0:
            ans = []
            for i in range(len(queue)):
                cur = queue.popleft()
                ans.append(cur.val)

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
            arr.append(ans)
        return arr
