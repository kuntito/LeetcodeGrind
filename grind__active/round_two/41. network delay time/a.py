# https://leetcode.com/problems/network-delay-time/

from typing import List

# i'm given three things..

# a 2d integer array, `times`
# an integer, `n`
# another integer, `k`

# let's start with the array, `times`
# each element of `times` has three values
# [start, destination, duration]

# all three, `start`, `destination` and `duration` are numbers

# `start` and `destination` represent nodes on a tree
# to get from `start` to `destination`, it takes `duration`

# now, the other two arguments, i'm given
# `n` and `k`

# `n` is the total number of nodes on the tree
# `k` is the origin.

# origin? yes.
# the question asks, if we start at point `k`
# what's the fastest time it would take, for us to travel to all the nodes.

# this is crazy.

# with, `times`, we can construct the tree.
# so we know the neighbours of every node.

# if we start at `k`
# what are we doing? to get the fastest time, we'd want to travel to all the closest nodes first.

# from those nodes, we'd want to travel to all their quickest nodes.

# and we'd keep going until we explore all the nodes..
# or there's no more nodes to explore..

# in which case, we'd have the fastest time, to explore all nodes connected to `k`
# the next question would be, did we touch all the nodes..

# because, it's possible, not all nodes are connected to `k`

# how would we address this? one way is to add all nodes to a set.
# i'm assuming all nodes are unique here.

# the question says all pairs (start, end) are unique
# but.. i don't know, i'd find out.

# if i create a set of all node values, `unseen`
# whenever, i explore any node, i'd remove it from `unseen`
# and carry on my exploration.

# the return statement would be based on whether `unseen` was empty.

# so how would you track the nodes. it's giving dijkstra.
# how so?

# at each point we want to track the closest node. the quickest node to reach.
# first off, we need a graph, of nodes to neighbours

# the first node would be `k`
# we'd append `k` to the minHeap.

# hmm.. i'm not to sure of this approach.
# why? because subsequent calls, the way i reasoned it during the walk
# need to be be paired..

# i'm spiralling.

# i'm using a minHeap to store all the nodes.
# sorted by duration.

# each minHeap item is at least two things.
# (duration, nodeValue)

# okay, so i start at `k`
# i pop from the minHeap
# i have it's duration and nodeValue

# i add it's duration to the a variable tracking duration so far, 
# let's call it `durationSoFar`

# then i check the min heap to see if there are more nodes with the same duration as the one i just popped.
# i'm doing this so i can grab all the nodes with that duration, since they'd all be reached at the same time.

# found a problem with this, i intended to set `0` as the initial duration for the first node.
# but what if it has neighbours that are also `0` duration.

# the question does say, duration could be as low as `0`
# what happens there.. well, it means, you'd explore them along with `k`
# i don't think it changes anything.

# if you start at `k` and there's a connected node with `0` duration.
# you might as well be starting at both nodes..

# alright, we keep balling.
# you pop out all nodes with the same duration.
# remove them from unseen.

# for each of those nodes, you can store them in a variable.. `layer`
# for every node in layer, you want to append their neighbours to the minHeap
# so we can repeat the process..

# this way, the minHeap always access the next closes layer.
# it updates `unseen`

# also, worth pointing out, you only want to include in layer
# the nodes that are `unseen`

# and you only add neighbours that are `unseen`

# you keep doing this until.. minHeap is empty..
# is this the case? yeah, eventually, you'd have addressed all neighbours

# and the loop ends.
# now, if unseen is empty, return the total duration you've tracked.
# if unseen has values, return `-1`

# made two errors
# one where i didn't make unseen a set, i simply assigned it to a range `(range(1, n + 1))`
# should've been `set(range(1, n + 1))`

# another error where while checking the minHeap for other nodes with a similar duration
# i didn't check to see if the minHeap had any values first
# and simply checked for `minHeap[0][0]`

# another two errors,
# while checking for the neighbours of each layer node..
# i didn't check the graph for the layer node, i did `graph[nei]` instead of `graph[layerNode]`

# the second error, while doing a min heap push
# i didn't add the minHeap in the arguments and simply did
# heapq.heappush((nei, dur))

# and i'm now noticing, i'm using a tuple for (nei, dur)
# when i used an array for the graph nodes..
# don't think this matters though.. i never add the graph nodes directly to the minHeap
# i unpack then convert to tuple.. should i be doing this? is a different question.

# and the test case failed.
# another error, where the "different question", bit me in the face
# i stored graph nodes as [nodeValue, duration]

# but heap nodes are meant to be [duration, nodeValue]
# when accessing graph nodes, i didn't switch the order and so the test case failed

# i've now switched the order
# but the test case still fails..

# TODO deep this example.. [[[1,2,1],[2,3,2],[1,3,2]], 3, 1],
# might have misunderstood the question.

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        unseen = set(range(1, n + 1))
        minHeap = [(0, k)]
        totalDuration = 0
        
        graph = self.getGraph(n, times)
        
        while minHeap:
            currSmallestDuration = minHeap[0][0]
            totalDuration += currSmallestDuration
            
            layer = []
            while minHeap and minHeap[0][0] == currSmallestDuration:
                _, layerNode = heapq.heappop(minHeap)
                if layerNode in unseen:
                    layer.append(layerNode)            
                    unseen.remove(layerNode)
                    
            for layerNode in layer:
                for nei, dur in graph[layerNode]:
                    if nei in unseen:
                        heapq.heappush(minHeap, (dur, nei))
    
    
        return -1 if unseen else totalDuration
                    
    def getGraph(self, n, times):
        graph = {}
        for node in range(1, n + 1):
            graph[node] = []
            
        
        for start, dest, duration in times:
            graph[start].append(
                [dest, duration]
            )
            
        return graph
    
arr = [
    [[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
    [[[1,2,1],[2,3,2],[1,3,2]], 3, 1],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.networkDelayTime(foo, bar, baz)
print(res)