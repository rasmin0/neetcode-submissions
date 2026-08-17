class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {}

        for u, v in trust:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
        
        indegree = [0] * (n + 1)

        for k, v in adj.items():
            for num in v:
                indegree[num] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == n - 1 and len(adj[i]) == 0:
                return i
        
        return -1