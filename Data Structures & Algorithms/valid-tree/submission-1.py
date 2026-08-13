class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}

        for src, dst in edges:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()
        
        def bfs(node):
            q = deque()

            q.append((node, None))
            visited.add(node)

            while q:
                cur, parent = q.popleft()

                for neighbor in adj.get(cur, []):
                    if neighbor == parent:
                        continue
                    if neighbor in visited and neighbor != parent:
                        return False
                    else:
                        q.append((neighbor, cur))
                        visited.add(neighbor)
            
            return True
        
        res = bfs(0)

        return res and len(visited) == n
                
