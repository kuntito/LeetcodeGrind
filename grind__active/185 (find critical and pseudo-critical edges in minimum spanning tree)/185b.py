# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/

# TODO https://neetcode.io/solutions/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
# 11:42
import heapq

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        # construct the graph
        # determine it's mst weight, `minWeight`
        
        # now, we want to find the mst weight if a single edge is removed
        # take turns excluding each edge
        # and check for the mst weight
        
        # if the weight increases,
        # the excluded edge is a critical node
        
        # grab the indices of all edges in the new mst
        # those would include critical and pseudo-critical edges
        
        # is it possible for an edge to be psuedo-critical and not be included in any mst?
        # well, if the edge weight is the same as others and they all happen to get picked instead of itself
        
        # but wouldn't the edge exclusion prevent this?
        # whichever edge is similar is bound to be removed at some point
        
        # not too sure about this one
        
        # how bout you establish the `minWeight`
        
        # then explore every combination of trees
        # it's giving.. recursion and backtracking
        # you track the edges so far,
        # you track the weights so far
        # and when you've formed a tree,
        # if the `mstWeight == minWeight`
        # then you put all the indices in a result array
        
        # this way we're bound to explore every edge
        
        graph = self.create_graph(n, edges)
        
        # visiualizing graph pairings
        # for i, v in graph.items():
        #     print(f'{i} => {[x[0] for x in v]}')
        
        # now, we get the mst weight
        mstWeight, edges = self.get_mst_weight(graph)
        print(mstWeight)
        print(edges)
        
        # start the exclusion and track 
        
    def get_mst_weight(self, graph):
        dim = len(graph)
        # to determine an mst
        # you start from any node
        # put the node in a minHeap
        # while `condition`
        # pick the shortest weight from the heap
        # this effectively means that node is the shortest from it's previous node
        
        # when starting the loop
        # there's only one item in the minHeap
        # so it's shortest by default
        # that said, the graph should be created with the weight as the first element
        
        # once we grab the node with the smallest weight
        # we append that node to a set, `seen`
        # then we explore it's neighbours
        # we add all unseen nodes to the heap
        
        # and repeat
        # we keep doing this until `len(seen) == dim`
        # at this point we've seen all the nodes
        
        # also, we'd have to be tracking the total weight so far
        
        totalWeight = 0
        seen = set()
        mstEdges = []
        
        # i'm assuming every node has an edge
        # `randomEdge` is one of the edges connecting to node `0`
        # i just need an edge to start the loop
        randomEdge = graph[0][0]
        minHeap = [randomEdge]
        
        
        while len(seen) < dim:
            weight, shortestNode, edgeIdx = heapq.heappop(minHeap)
            if shortestNode in seen: continue
            seen.add(shortestNode)
            print(shortestNode)
            # TODO your code is inaccurate
            # on the first iteration, which weight are you referring to
            # a weight is between two edges, if you have a single edge in the heap
            # how are you adding weight?
            totalWeight += weight
            mstEdges.append(edgeIdx)
            
            for nei in graph[shortestNode]:
                neiNode = nei[1]
                
                if neiNode in seen: continue
                heapq.heappush(minHeap, nei)
                
        return totalWeight, mstEdges
        
        
    def create_graph(self, n, edges):
        # we can create the graph
        # but also need a way to identify edges by indices
        # the graph is `node => [other nodes plus weights]`
        # so we could do (otherNode, weight, index)
        graph = {}
        
        for i in range(n):
            graph[i] = []
            
        dim = len(edges)
        for idx in range(dim):
            node, otherNode, weight = edges[idx]
            graph[node].append(
                (weight, otherNode, idx)
            )
            graph[otherNode].append(
                (weight, node, idx)
            )
            
        return graph
    
arr = [
    [5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findCriticalAndPseudoCriticalEdges(foo, bar)