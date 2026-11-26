from typing import List
import heapq

class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:
        pass
        # first every node should know it's destinations.
        self.graph = self.getGraph(edges)
        
        # now, what, iterate through every node.
        self.solutions = []
        for node in self.graph:
            self.explore(node)
            
        critical = set(range(n))
        pseudocritical = set()
        
        for s in self.solutions:
            for n in s:
                if n not in critical:
                    pseudocritical.add(n)
                    
        return list(critical), list(pseudocritical)
    
    def explore(self, node):
        # what are doing here?
        # destinations.
        
        # what is each item, (cost, node, weight, edgeIdx)
        destinations = [(0, node, 0, )]
        
    
        
        

    
arr = [
    [
        5,
        [
            [0,1,1],
            [1,2,1],
            [2,3,2],
            [0,3,2],
            [0,4,3],
            [3,4,3],
            [1,4,6]
        ],
    ],
    [
        4,
        [
            [0,1,1],
            [1,2,1],
            [2,3,1],
            [0,3,1]
        ],
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findCriticalAndPseudoCriticalEdges(foo, bar)
print(res)