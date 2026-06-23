class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones, zeros = 0, 0

        for i in range(len(students)):
            if students[i] == 0:
                zeros += 1
            else:
                ones += 1

        q = deque(sandwiches)

        for i in range(len(q)):
            if q[i] == 0:
                if zeros > 0:
                    zeros -= 1
                else:
                    break
            else:
                if ones > 0:
                    ones -= 1
                else:
                    break
        print(ones)
        print(zeros)
        return max(ones, zeros)


