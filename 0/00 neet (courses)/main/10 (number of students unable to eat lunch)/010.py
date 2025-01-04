# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
from collections import Counter

class Solution:
    def get_uno_cero(self, arr):
        uno = sum(1 for i in arr if i)
        return uno, len(arr) - uno

    def countStudents(self, students, sandwiches):
        uno_stud, cero_stud = self.get_uno_cero(students)
        
        for n in sandwiches:
            if n and uno_stud:
                uno_stud -= 1
            elif not n and cero_stud:
                cero_stud -= 1
            else:
                 break

        return uno_stud + cero_stud

    def countStudentsII(self, students, sandwiches):
        student_map = Counter(students)
        total_students = len(students)

        for n in sandwiches:
            if student_map[n] > 0:
                student_map[n] -= 1
                total_students -= 1
            else:
                break
        return total_students

# students = [1, 1, 0, 0]
# sandwiches = [0, 1, 0, 1]

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

foo = Solution()
res = foo.countStudents(students, sandwiches)
print(res)



