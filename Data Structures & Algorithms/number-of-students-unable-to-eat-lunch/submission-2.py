class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sandwiches in a stack
        # students in a queue

        stQ = deque(students)
        saQ = deque(sandwiches)
        i = 0

        while stQ:
            if i == (50 * len(stQ)):
                break
            if stQ[0] == saQ[0]:
                stQ.popleft()
                saQ.popleft()
            else:
                x = stQ.popleft()
                stQ.append(x)
                i += 1
        
        return len(stQ)


        # students = [1,1,1]
        # sandwiches = [0,1,1]


