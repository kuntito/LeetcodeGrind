# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1 for _ in range(n)]

        for uno, dos in edges:
            uno_parent = self.get_parent(uno, parents)
            dos_parent = self.get_parent(dos, parents)

            if uno_parent == dos_parent:
                continue
            if ranks[uno_parent] > ranks[dos_parent]:
                # `dos_parent` should become a child of `uno_parent`
                parents[dos_parent] = uno_parent
                # `uno_parent` rank += `dos_parent` rank
                ranks[uno_parent] += ranks[dos_parent]
                pass
            else:
                # `uno_parent` should become a child of `dos_parent`
                parents[uno_parent] = dos_parent 
                # `dos_parent` rank += `uno_parent` rank
                ranks[dos_parent] += ranks[uno_parent]
                pass

            n -= 1

        return n
    
    def get_parent(self, node, parents):
        while node != parents[node]:
            node = parents[node]

        return node
    

arr = [
    [3, [[0, 1], [0, 2]]],
    [6, [[0, 1],[1, 2], [2, 3], [4, 5]]],
    [5, [[1,2],[2,3],[4,5],[1,4]]], #TODO draw out the union
]
foo, bar = arr[-1]
sol = Solution()
res = sol.countComponents(foo, bar)
print(res)