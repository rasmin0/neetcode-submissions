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
            return
        cur = head
        newHead = Node(head.val)

        cur = cur.next
        cur1 = newHead

        myMap = {head : newHead}

        while cur:
            cur1.next = Node(cur.val, cur.next)
            cur1 = cur1.next
            myMap[cur] = cur1
            cur = cur.next
        
        cur = head
        while cur:
            if cur.random == None:
                myMap[cur].random = None
            else:
                myMap[cur].random = myMap[cur.random]
            cur = cur.next

        return myMap[head]
        


            