class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set()

        for src, dst in edges:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
            adj[dst].append(src)

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
        num = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                num += 1
        
        return num

