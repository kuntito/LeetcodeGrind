from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:
        self.nodeCount = n
        self.graph = self.createGraph(edges)
        
        # for k in self.graph:
        #     item = self.graph[k]
        #     print(k, end=" => ")
        #     for neiNode, _, _ in item:
        #         print(neiNode, end=", ")
        #     print()
        
        # what do i wanna do?
        # to explore every MST.
        # start an MST from every node.
        # and for each node, hold the solution edge set.
        # this would be a hashmap.
        # and one for the total MST count.
        self.solutionPool = set()
        self.solutionSet = defaultdict(int)
        
        for node in range(n):
            self.exploreMstFrom(node)
                    
        self.populateSolutionSet()
    
        print(self.solutionSet)
    
        totalMsts = self.solutionSet[-1]
        
        critical, pseudo = [], []
        for edge, mstPresence in self.solutionSet.items():
            if edge == -1: continue
            
            if mstPresence == totalMsts:
                critical.append(edge)
            else:
                pseudo.append(edge)
                
        return critical, pseudo
    
    
    def populateSolutionSet(self):
        for edgeSet in self.solutionPool:
            for edge in edgeSet:
                self.solutionSet[edge] += 1
                
                


    def createGraph(self, edges):
        graph = defaultdict(list)
        
        for edgeIdx, item in enumerate(edges):
            nodeOne, nodeTwo, weight = item
            
            graph[nodeOne].append(
                (nodeTwo, weight, edgeIdx)
            )
            graph[nodeTwo].append(            
                (nodeOne, weight, edgeIdx)
            )
            
        return graph


    def exploreMstFrom(self, startNode):
        pass
        # now, i've picked this as the starting point
        # where are the destinations.
        # can i make it the first destination.
        # well, yes.
        # you need the item
        # (cost, nextNode, edgeIdx)
        
        initItem = (0, startNode, -1)
        destinations = [initItem]
        
        seen = set()
        setOfEdges = set()
        
        while len(seen) < self.nodeCount:
            sameCost = []
            curCost = destinations[0][0]        
            while destinations and destinations[0][0] == curCost:
                item = heapq.heappop(destinations)
                sameCost.append(item)

            if len(sameCost) == 1:
                curCost, curNode, edgeIdx = sameCost[0]
                            
                if curNode in seen: continue
                seen.add(curNode)
                setOfEdges.add(edgeIdx)
                
                for item in self.graph[curNode]:
                    furtherDestination, weight, edgeIdx = item
                    if furtherDestination in seen: continue
                    
                    heapq.heappush(
                        destinations,
                        (
                            curCost + weight,
                            furtherDestination,
                            edgeIdx,    
                        )
                    )
            else:
                for curCost, curNode, edgeIdx in sameCost:
                    self.exploreFurther()
                    
                return

        mstEdges = tuple(setOfEdges)
        print(f'{startNode} => {mstEdges}')
        self.solutionPool.add(
            mstEdges                
        )
            
        
    
        
        

    
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