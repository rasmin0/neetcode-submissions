class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set()

        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque()
            
            q.append(node)
            visited.add(node)

            while q:
                cur = q.popleft()

                for neighbor in adj.get(cur, []):
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)

        c = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                c += 1
        
        return c
        
