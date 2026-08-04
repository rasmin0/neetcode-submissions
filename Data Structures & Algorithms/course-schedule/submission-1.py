class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make a graph using adjList
        adjList = {}
        indegree = [0] * numCourses
        
        for dst, src in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)
            indegree[dst] += 1 
        
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()

            for neighbor in adjList.get(cur, []):
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        for num in indegree:
            if num > 0:
                return False
        
        return True
        

