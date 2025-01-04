# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = {}

        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # print(graph)

        seen = set()
        count = 0
        for i in range(n):
            if i in seen:
                continue
            self.explore(i, graph, seen)
            count += 1

        return count
    

    def explore(self, i, graph, seen):
        if i in seen:
            return
        
        seen.add(i)
        for nei in graph[i]:
            self.explore(nei, graph, seen)


arr = [
    [[0, 1],[1, 2], [2, 3], [4, 5]],
    [[0, 1], [0, 2]],
]
foo = arr[-1]
sol = Solution()
res = sol.countComponents(3, foo)
print(res)