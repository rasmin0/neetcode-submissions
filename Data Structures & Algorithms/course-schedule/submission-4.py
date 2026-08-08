class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for dst, src in prerequisites:
            if dst not in adjList:
                adjList[dst] = []
            if src not in adjList:
                adjList[src] = []
            adjList[src].append(dst)
        print(adjList)
        
        indegree = numCourses * [0]

        for k, v in adjList.items():
            for num in v:
                indegree[num] += 1
        
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
            if num == 1:
                return False
        
        return True


