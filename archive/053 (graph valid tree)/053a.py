# https://leetcode.com/problems/graph-valid-tree/description/


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adj = {}

        for i in range(n):
            adj[i] = []

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
    
        seen = set()
        if self.explore(0, None, adj, seen):
            return False
            
        return len(edges) == n-1
    
    
    def explore(self, node, parent, adj, seen):
        if node in seen:
            return True
        
        seen.add(node)
        for nei in adj[node]:
            if nei == parent:
                continue

            if self.explore(nei, node, adj, seen):
                return True
            
        return False
    

arr = [
    [5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
    [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]],
    [5, [[0,1],[1,3],[3,0],[2,4]]],
]
foo, bar = arr[-1]
sol = Solution()
arr = sol.validTree(foo, bar)
print(arr)