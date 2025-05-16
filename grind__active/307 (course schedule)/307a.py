# https://leetcode.com/problems/course-schedule/description/

# what are doing? we want to implement a function `canFinish`
# the function takes two arguments, an integer `numCourses` and a 2d list of integers, `prerequisites`

# the situation is, there's `numCourses` to take, labelled from 0 till numCourses - 1
# and each element of prerequesites, has two elements [a, b], where `a` and `b` are labels for individual courses

# what this means is, to take course `a`, one must first take course `b`
# `b` is a prerequisite to course `a`

# our job is to find out if all the courses can be taken
# consider prerequisites = [[1, 0]]
# this means we need to take `0` before taking `1`, this works fine so we return True

# consider [[1, 0], [0, 1]]
# this means we need to take `0` before taking `1`
# this also means we need to take `1` before taking `0`
# which creats a cicular dependency, `1` needs `0`, `0` needs `1`
# this won't work so we return False


# it's looking like a graph problem
# where we connect all courses to their prerequisites
# then we try to explore all courses, if this is possible without encountering a cycle
# then yes, we can finish all courses

# TODO deep the run time and space time

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pass

        # we need a graph, let's use a helper function
        graph = self.getGraph(prerequisites, numCourses)

        # then we explore all the courses
        # for each course we want to explore it's prerequisites first
        # post order traversal
        # we need to track courses we've visited to speed things up
        # and to find cycles, we need to track courses in each traversal path
        # if we find a cycle, we return True
        visited, visiting = set(), set()
        for c in range(numCourses):
            if self.exploreCycle(c, graph, visited, visiting):
                return False

        return True

    def exploreCycle(self, course, graph, visited, visiting):
        if course in visited:
            return False
        if course in visiting:
            return True

        visiting.add(course)
        for preq in graph[course]:
            if self.exploreCycle(preq, graph, visited, visiting):
                return True

        visiting.remove(course)
        visited.add(course)

    def getGraph(self, prerequisites, numCourses):
        graph = {}
        for c in range(numCourses):
            graph[c] = []

        for crs, preq in prerequisites:
            graph[crs].append(preq)

        return graph


arr = [
    [2, [[1, 0], [0, 1]]],
    [2, [[1, 0]]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.canFinish(foo, bar)
print(res)
