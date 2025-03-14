# https://leetcode.com/problems/redundant-connection/description/
from collections import deque

class Solution:
    def findRedundantConnection(self, edges: list) -> list:
        self.parents = {}
        self.ranks = {}

        for n in range(1, len(edges) + 1):
            self.parents[n] = n
            self.ranks[n] = 1

        for e in edges:
            if not self.add_edge(e):
                return e

    def add_edge(self, edge):
        uno, dos = self.find_parent(edge[0]), self.find_parent(edge[1])
        if uno == dos:
            return False
        
        if self.ranks[uno] > self.ranks[dos]:
            self.parents[dos] = uno
        elif self.ranks[dos] > self.ranks[uno]:
            self.parents[uno] = dos
        else:
            self.parents[dos] = uno
            self.ranks[uno] += 1

        return True

    def find_parent(self, node) -> int:
        parent = self.parents[node]

        while parent != self.parents[parent]:
            # self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    

arr = [
    [[1, 2], [1, 3], [2, 3]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]],
]
foo = arr[-1]
sol = Solution()
res = sol.findRedundantConnection(foo)

print(res)