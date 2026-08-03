"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        newHead = Node(head.val)
        cur1 = head
        cur2 = newHead

        copy = {head : newHead}

        cur1 = cur1.next

        while cur1:
            newNode = Node(cur1.val)
            cur2.next = newNode
            copy[cur1] = newNode
            cur1 = cur1.next
            cur2 = cur2.next
        
        cur1 = head

        while cur1:
            if cur1.random is None:
                copy[cur1].random = None
            else:
                copy[cur1].random = copy[cur1.random]
            cur1 = cur1.next
        
        return newHead