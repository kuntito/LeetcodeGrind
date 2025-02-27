# https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# https://neetcode.io/solutions/construct-quad-tree
# TODO deep the question and the solution
class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        pass
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            
            if allSame:
                return Node(grid[r][c], True)
            
            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)
            
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        
        dim = len(grid)
        return dfs(dim, 0, 0)