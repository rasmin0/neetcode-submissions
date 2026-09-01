class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # make adj list
        # make indegree array
        # queue nodes which have an indegree of 0
        # run topological sort algorithm
        # decrement indegree of visited nodes
        # queue nodes with indegree of 0

        adj = {}
        for dst, src in prerequisites:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
        
        indegree = [0] * numCourses
        res = []

        for k, v in adj.items():
            for num in v:
                indegree[num] += 1
        
        q = deque()
        visited = set()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)
                res.append(i)
        
        while q:
            cur = q.popleft()

            for neighbor in adj.get(cur, []):
                if neighbor not in visited:
                    indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)
                    res.append(neighbor)
        
        for num in indegree:
            if num != 0:
                return []
        
        return res
