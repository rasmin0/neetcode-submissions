class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for dst, src in prerequisites:
            if dst not in adj:
                adj[dst] = []
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)

        indegree = [0] * numCourses

        for k, v in adj.items():
            for node in v:
                indegree[node] += 1

        q = deque()
        visited = set()
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)
                res.append(i)
        

        while q:
            cur = q.popleft()

            for neighbor in adj.get(cur, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)
                    res.append(neighbor)
        
        for num in indegree:
            if num != 0:
                return []
        return res
                

