# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/

from collections import defaultdict
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        # construct a graph
        graph = self.getGraph(edges)
        
        # convert all edges to tuples for hashing
        # since edges are bidirectional, we'd need two tuples for each edge
        # `(a, b, wgt) and (b, a, wgt)`
        edgeTuples = []
        for a, b, wgt in edges:
            uno = (a, b, wgt)
            dos = (b, a, wgt)
            
            edgeTuples.append(uno)
            edgeTuples.append(dos)
        
        # find the MST in the graph, save it's weight, `targetWeight`
        mstWeight = self.getMstWeight(graph)
        
        # store all the edges in a set, `allEdges`
        
        # for each edge, find the graph MST without it
        # FIXME you can't just remove any edge
        # you need to remove edges in a way that all nodes are still connected
        # else it is futile
        
        # iterate through the edges and find the MST weight without that edge
        # if the weight is equal to `targetWeight`
        # store all the edges in a set, `allEdges`
        
    def getGraph(self, edges):
        graph = defaultdict(list)
        
        for a, b, wgt in edges:
            graph[a].append([b, wgt])
            graph[b].append([a, wgt])
            
        return graph