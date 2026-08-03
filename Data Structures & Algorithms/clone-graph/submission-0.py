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
        copy = {node : Node(node.val)}

        while q:
            sizeQ = len(q)

            for _ in range(sizeQ):
                cur = q.popleft()

                for neighbor in cur.neighbors:
                    if neighbor not in copy:
                        copy[neighbor] = Node(neighbor.val)
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                    copy[cur].neighbors.append(copy[neighbor])

        return copy[node]

        