class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff(s1, s2):
            dist = 0

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    dist += 1
            
            return dist
        

        q = deque()
        visited = set()

        q.append(beginWord)
        visited.add(beginWord)

        transformations = 1

        while q:
            size = len(q)

            for _ in range(size):
                cur = q.popleft()
                
                for s in wordList:
                    res = diff(cur, s)

                    if res == 1 and s not in visited:
                        q.append(s)
                        visited.add(s)

                        if s == endWord:
                            return transformations + 1

            transformations += 1
        
        return 0