class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def bfs(src, dst):
            visited = set()
            q = deque()

            q.append(src)
            visited.add(src)

            while q:
                cur = q.popleft()

                for neighbor in adj.get(cur, []):
                    if neighbor == dst:
                        return True
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            return False
            

        adj = {}
        res = []

        for src, dst in edges:
            if not bfs(src, dst):
                if src not in adj:
                    adj[src] = []
                if dst not in adj:
                    adj[dst] = []
                adj[dst].append(src)
                adj[src].append(dst)
            else:
                res.append([src, dst])
            
        
        return res[-1]
        
        

        