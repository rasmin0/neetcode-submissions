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
        
        q = deque()
        visited = set()
        q.append(node)
        visited.add(node)
        clones = {node : Node(node.val)}

        while q:
            sizeQ = len(q)

            for _ in range(sizeQ):
                cur = q.popleft()

                for neighbor in cur.neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                    if cur not in clones:
                        clones[cur] = Node(cur.val)
                    if neighbor not in clones:
                        clones[neighbor] = Node(neighbor.val)
                    clones[cur].neighbors.append(clones[neighbor])
        
        return clones[node]

