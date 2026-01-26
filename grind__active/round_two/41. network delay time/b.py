# https://leetcode.com/problems/network-delay-time/description/

from typing import List

# what's going on?

# i'm given three things..
# a 2d array, `times`
# an integer, `n`, and..
# another integer, `k`

# what do these things mean..
# starting with the array... each element is three-tiered.

# [startNode, destNode, duration]

# the names are eponymous, each element represents edges of a graph.
# you start at `startNode`, you go to `destNode`, it takes `duration` to get there..

# okay, what about the other variables, `n` and `k`
# `n` is the total number of nodes, each node is an integer..
# okay, and `k`

# `k` is the starting node..
# we want to explore.. starting at `k`
# what's the fastest time we can reach every node within the graph..

# if it's not possible, return `-1`
# if it is, return the value..

# so how would the code go..
# first, i need to create the graph..

# then what, start iteration from node `k`
# i should probably rename it to `originNode`

# so from, `originNode`, what are we doing..
# we want to explore the closest nodes..
# nodes? yes, we're exploring multiple nodes with the same duration...

# the idea, we're sending information to all the nodes
# and want to know how quickly we can get to all the nodes..

# if `originNode` is has two nodes with the same duration..
# both nodes would receive the information at the same time..

# i know Dijkstra's algo can help here..
# what we doing is selecting by the nearest nodes..

# okay.. each iteration, we'd pop all the nodes with the same value..
# it's a layer of nodes, with the same value..

# explore their children and add to the minHeap

# what would the minHeap store..

# [duration, currentNode]

# all nodes are unique i believe..
# ..

# let's rewind a bit..
# say you start at .. what's the first entry into your minHeap

# first entry is [0, originNode]

# okay, so the iteration would be.. grab all the nodes with `0` duration..
# in our case.. only one..

# then we'd add `originNode` to `seen`
# once, we've explored a node, the min heap exploration ensures we always
# take the smallest path to any node, hence no need to re-explore it..

# if the node is already seen, we ball..

# so for all the nodes that match the smallest duration..
# we grab all their neighbours and append to the minHeap

# but the duration we'd be adding is what?

# the sum of the duration it took to get to the parent..
# plus the duration from parent to neighbour..

# this way, each node contains the duration from origin..
# and we keep doing this till we exhaust all the connected nodes..

# we'd also need to track total duration so far..
# technicall the last node we see should contain this information..

# but it could have neighbours that.. i'm not sure where this leads..
# but i know if i declare a variable to track `totalDuration`

# i'm good..

# anything else.. well, we want to return `totalDuration` only if 
# `len(seen) == n`, meaning we've visited all the nodes, if not, return `-1`

# let's code

# made a mistake, while grabbing the layer nodes.. i accessed minHeap[0][0]
# without checking `minHeap` still had values..

# FIXME another mistake, with the way i'm updating `currentDur`
# i currently use this to track the total duration..
# but it's inaccurate cause..

# once you explore all connected nodes.. 
# it's possibly the minHeap still has values..
# the example, `[[[1,2,1],[2,3,2],[1,3,2]], 3, 1]` is a case study..
# we start at `1`
# we append the neighbours (2 and 3) to the heap
# we explore 2 next, it's neighbour is also 3 but a shoter path

# now the heap has (3, 3)
# but only one of the threes is shortes..
# we realize that when we explore the `3`

# but since the heap still has one more (3)
# the loop demands we still explore this..
# and is where the problem lies..

# the first line, `currentDur = minHeap[0][0]`
# always updates the duration to the first node..
# and here, we would be updating current duration to the longer `3`

# i fixed this by setting a variable outside the loop, `res`
# and this is only updated when we have nodes in `layer`
# meaning the topmost minHeap value is only valid when there's nodes in the layer

# the layer represents unexplored nodes..
# there's probably a cleaner way to write this and that's what you'd want to do on next visit..


import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        
        # `k` is the origin node
        firstItem = (0, k)
        
        heapq.heappush(minHeap, firstItem)
        seen = set()
        currentDur = 0
        
        graph = self.getGraph(n, times)
        
        while minHeap:
            currentDur = minHeap[0][0]
            
            layer = []
            # we want all the nodes with this current duration
            while minHeap and minHeap[0][0] == currentDur:
                _, layerNode = heapq.heappop(minHeap)
                if layerNode in seen: continue

                layer.append(layerNode)
                seen.add(layerNode)
                
            # now, we want to explore the neighbours of each layer node
            # need the graph..
            
            for node in layer:
                for neiDest, neiDur in graph[node]:
                    pass
                    # now we add to minHeap..
                    # but amend the duration to include the parent's duration..
                    # since all elements in layer, have the same duration..
                    # `currentDur` would do
                    
                    # as an optimization, we want to avoid seen neighbours
                    if neiDest in seen:
                        continue
                    
                    heapq.heappush(
                        minHeap,
                        (
                            currentDur + neiDur,
                            neiDest,
                        )
                    )
        return currentDur if len(seen) == n else -1
            
            
    def getGraph(self, nodeCount, edges):
        # how we doing this?
        # key, value pair
        graph = {}
        
        # key is startNode
        # value is [destNode, duration]
        
        # need to add all nodes into graph with an empty value pair
        # in case there's disconnected nodes..
        
        # if there was, you wouldn't touch it.. would you..
        # how so.. you only explore graph, if it's a neighbour..
        # yes, it can be a neighbour and not point to anything..
        
        # unless i want to do `if nei in graph` first..
        # then it makes sense to add all nodes from the jump..
        # aii..
        
        for n in range(1, nodeCount + 1):
            graph[n] = []
        
        for startNode, destNode, duration in edges:
            graph[startNode].append(
                [destNode, duration]
            )
            
        return graph
    
arr = [
    [[[1,2,1],[2,3,2],[1,3,2]], 3, 1],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.networkDelayTime(foo, bar, baz)
print(res)
            