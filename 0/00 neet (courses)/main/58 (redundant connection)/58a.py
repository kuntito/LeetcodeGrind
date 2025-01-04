# https://leetcode.com/problems/redundant-connection/description/
from collections import deque

class Solution:
    def findRedundantConnection(self, edges: list) -> list:
        aj_list = self.get_adjacency_list(edges)

        node = edges[0][0]
        cycle_queue = []
        seen = set()
        self.explore_cycle(node, aj_list, cycle_queue, seen)

        for e in edges[::-1]:
            if e[0] in seen and e[1] in seen:
                return e
            

    def explore_cycle(self, node, aj_list, cycle_queue, seen, parent = None):
        if node in seen:
            for elem in cycle_queue:
                if elem == node:
                    break
                seen.remove(elem)

            return True
        
        seen.add(node)
        cycle_queue.append(node)

        for child in aj_list[node]:
            if child == parent: continue

            if self.explore_cycle(
                child,
                aj_list,
                cycle_queue,
                seen,
                node
            ): return True

            seen.remove(child)
            cycle_queue.pop()

        return False


    def get_adjacency_list(self, edges: list):
        adjacency_list = {}
        for e in edges:
            first, second = e
            if first not in adjacency_list:
                adjacency_list[first] = []
            if second not in adjacency_list:
                adjacency_list[second] = []

            adjacency_list[first].append(second)
            adjacency_list[second].append(first)

        return adjacency_list


arr = [
    [[1, 2], [1, 3], [2, 3]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]],
]
foo = arr[-1]
sol = Solution()
res = sol.findRedundantConnection(foo)

print(res)
            
