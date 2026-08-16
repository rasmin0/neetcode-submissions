class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {}

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
        
        count = 0

        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1
        return count

        