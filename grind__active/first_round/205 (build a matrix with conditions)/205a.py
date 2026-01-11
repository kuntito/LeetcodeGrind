# https://leetcode.com/problems/build-a-matrix-with-conditions/description/

# TODO https://neetcode.io/solutions/build-a-matrix-with-conditions
# TODO, the code is accepted, but rewrite to deep it
from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        pass
    
        # it's giving topological sort
        # determine a rowGraph
        # one order i which items can exist along the rows
        
        # determine the colGraph
        # one order in which items can exist along the columns
        
        
        # once you have this
        # deduce which items should be on what row
        # you might need a hashmap to pair items with row indices
        
        # once you have this, declare a global variable
        # `self.last_ci`
        # use the column graph to place the leaf node
        # use the hash map to determine the leaf's row
        # on that row, place the value at `self.last_ci`
        # then decrement `self.last_ci`
        
        # repeat this till you exhaust all elements of the column graph
        # if you couldn't place all the elements from either rowGraph or columnGraph, return an empty matrix
        
        # step one, rowGraph
        rowGraph = self.createRowGraph(rowConditions, k)
        colGraph = self.createColGraph(colConditions, k)
        
        # for i, v in rowGraph.items():
        #     print(f'{i} => {v}')
        
        # step two, get a topological order of rows
        
        rowOrder = self.getTopological(rowGraph)
        if not rowOrder:
            return []
        colOrder = self.getTopological(colGraph)
        if not colOrder:
            return []
                
        rowMap = {n:idx for idx, n in enumerate(rowOrder)}
        colMap = {n:idx for idx, n in enumerate(colOrder)}
        
        # step two point five, create grid
        grid = [[0 for _ in range(k)] for _ in range(k)]
        
        # step three, pair number with coordinates
        for i in range(1, k+1):
            ri = rowMap[i]
            ci = colMap[i]
            grid[ri][ci] = i
            
        return grid
            
        
        
    def getTopological(self, graph):
        topologicalOrder = deque()
        
        seen = set()
        visiting = set()
        for n in graph:
            if not self.explore(n, graph, seen, visiting, topologicalOrder):
                return False
            
        return topologicalOrder
    
    def explore(self, node, graph, seen, visiting,order):
        if node in seen:
            return True
        if node in visiting:
            return False
        visiting.add(node)
        
        for nei in graph[node]:
            if not self.explore(nei, graph, seen, visiting, order):
                return False
            
        visiting.remove(node)
        
        seen.add(node)
        order.appendleft(node)
        
        return True
        

        
    def createRowGraph(self, rowConditions, k):
        graph = {}
        for i in range(1, k + 1):
            graph[i] = []
            
        for top, bottom in rowConditions:
            graph[top].append(bottom)
        return graph
            
    def createColGraph(self, colConditions, k):
        graph = {}
        for i in range(1, k + 1):
            graph[i] = []
            
        for left, right in colConditions:
            graph[left].append(right)
            
        return graph


arr = [
    [3, [[1,2],[3,2]], [[2,1],[3,2]]],
    [3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.buildMatrix(foo, bar, baz)

for row in res:
    print(row)
