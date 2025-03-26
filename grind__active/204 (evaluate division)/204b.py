# https://leetcode.com/problems/evaluate-division/description/

from collections import defaultdict, deque

# https://neetcode.io/solutions/evaluate-division
# TODO deep solution
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        adj = defaultdict(list)  # Map a -> list of [b, a/b]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]

                
            

arr = [
    [
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.calcEquation(foo, bar, baz)
print(res)