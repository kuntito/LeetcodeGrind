from typing import List
import heapq

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # put the weights first, so i can heapify.
        # need the indices of the edges too.
        connections = []
        for idx, item in enumerate(edges):
            a, b, w = item
            connections.append((
                w,
                a,
                b,
                idx
            ))
        
        heapq.heapify(connections)
        
        
        seen = {}
        critical = set()
        pseudocritical = set()
        
        while connections:
            w, a, b, idx = heapq.heappop(connections)

            if a in seen and b in seen:
                if w == seen[a][0]:
                    foo = seen[a][1]
                    if foo in critical:
                        critical.remove(foo)
                    pseudocritical.add(foo)
                    pseudocritical.add(idx)
                    
                if w == seen[b][0]:
                    foo = seen[b][1]
                    if foo in critical:
                        critical.remove(foo)
                    pseudocritical.add(foo)
                    pseudocritical.add(idx)
            elif a in seen:
                seen[b] = (w, idx)
                critical.add(idx)
            elif b in seen:
                seen[a] = (w, idx)
                critical.add(idx)
            else:
                seen[a] = (w, idx)
                seen[b] = (w, idx)
                
                critical.add(idx)
                
            
            
        return [list(critical), list(pseudocritical)]
    
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