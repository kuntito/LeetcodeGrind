# https://leetcode.com/problems/network-delay-time/
from typing import List

# here, we have three things..
# a 2d grid, `times`, and two integers, `n` and `k`

# each element of the grid is three-tiered, [a, b, c]
# where:
# a = start node
# b = end node
# c = time it takes from start node to end node..

# the 2d grid represents a graph.

# and `n` is the number of nodes in the graph
# `k` is the starting node.

# the question is, if i start at `k`
# what's the minimum time it would take me to get to all the nodes..
# i should return that value.

# and if i can't reach all the nodes, return -1

# my previous approach, was i'd find the nearest nodes with the same duration.
# place them in an array..

# iterate through that array, for each node, i'd append it's neighbours to a minHeap
# subsequent cells get their values from this min heap.

# i did it this way, because i'd travel from `k`to all nodes with the same duration at the same time.
# and that duration is the current time during the traversal.

# however, things could be simpler.
# just append the next node to the minHeap..
# what if two nodes have the same duration from `k`
# well, they'd both in the minHeap but explored at different times..

# and how would this affect the current duration..
# your current duration is always the node you're exploring.

# track nodes you've seen
# and every node you explore next is the shortest time it'd take to get to that node.

# worth mentioning, what you add to the heap isn't the node distance itself,
# but the distance of it's parent plus node distance.

# and how'd this look in code.
# first a graph of neighbours, place all nodes in a dictionary
# the key is node integer
# value is [distance, neiNode]

# then a minHeap..
# initialize the minHeap with [0, k]

# a set to track seen nodes..
# end a day, return the tracked value, if the number of seen nodes  == n
# meaning we seen all the nodes, if not, return -1


# syntax error, used single `=` stead of double, `==`
#  did `if len(seen) = n`
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.getGraph(n, times)
        
        minHeap = [(0, k)]
        seen = set()
        
        quickestTime = 0
        while minHeap:
            curDist, curVal = heapq.heappop(minHeap)
            
            if curVal in seen:
                continue
            
            quickestTime = curDist
            seen.add(curVal)
            
            for neiDist, neiVal in graph[curVal]:
                heapq.heappush(
                    minHeap,
                    (
                        neiDist + curDist,
                        neiVal,
                    )
                )
                
        return quickestTime if len(seen) == n else -1
                
        
    def getGraph(self, n, times):
        graph = {}
        
        for i in range(1, n+1):
            graph[i] = []

        for startNode, endNode, dist in times:
            graph[startNode].append((dist, endNode))
            
        return graph