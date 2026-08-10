"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        newNode = Node(node.val)
        clone= {node : newNode}

        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()

            for neighbor in cur.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clone[neighbor].neighbors.append(clone[cur])
        
        return clone[node]

    