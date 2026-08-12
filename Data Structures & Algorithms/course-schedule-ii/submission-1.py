class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        res = []

        for post, pre in prerequisites:
            if post not in courses:
                courses[post] = []
            if pre not in courses:
                courses[pre] = []
            courses[pre].append(post)
        
        indegree = [0] * numCourses

        for k, v in courses.items():
            for num in v:
                indegree[num] += 1
        
        visited = set()
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)
                res.append(i)
        
        while q:
            cur = q.popleft()

            for neighbor in courses.get(cur, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 and neighbor not in visited:
                    q.append(neighbor)
                    res.append(neighbor)
                    visited.add(neighbor)
        
        for num in indegree:
            if num != 0:
                return []
                
        return res
        
