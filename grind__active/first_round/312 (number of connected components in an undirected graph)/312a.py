# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

from typing import List

# i want to implement a function `countComponents`
# it takes two arguments, an integer `n` that represents the number of nodes in a graph
# and a 2d integer array that represents the edges of said graph

# each element of the 2d array can be represented as `edges[i] = [a, b]`
# where `a` and `b` are connected nodes in the graph

# to solve this i want to connect all the edges
# an adjacency list can represent the connection between edges

# since i know there's `n` nodes, i can create a set of `n` nodes
# the set would contain elements from `0 to n-1`
# the set would represent unvisited nodes

# since i have a graph and i know the edges are undirected, if i pick a single node `a`
# it means i can explore all it's connected components
# for every visited node, i'd remove it from `unvisited`

# so everytime i explore a node, i'm effectively exploring a connected component
# this way i can keep track of the number of connected components

# space time complexity:
# initializing the graph with all the nodes is O(n)
# running through the number of edges is O(e) where is `e` is number of edges
# so O(n + e)

# run time complexity:
# O(n + e) to create the graph
# what's the iteration like
# technically, i'd only have to explore each node once
# so... O(n)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass
        graph = self.getGraph(n, edges)
        
        count = 0
        # unvisited should be initialized to a set of all the nodes
        unvisited = set(range(n))
        for node in range(n):
            if node in unvisited:
                self.explore(node, graph, unvisited)
                count += 1
                
        return count
    
    def getGraph(self, n, edges):
        # declare the graph
        graph = {}
        # add every node to the graph
        for node in range(n):
            graph[node] = []
            
        # add edges to each node
        for one, two in edges:
            graph[one].append(two)
            graph[two].append(one)
            
        return graph
        
    
    def explore(self, node, graph, unvisited):
        # we only want to explore unvisited nodes
        if node not in unvisited:
            return
        
        unvisited.remove(node)
        
        for nei in graph[node]:
            # to avoid extra recursive calls
            # in that case, do we need the initial call
            # yes, because the root function requires us to explore all nodes
            # and since we explore every node in a tree
            # it's possible we try to explore a node already explored
            if nei in unvisited:
                self.explore(nei, graph, unvisited)
                
                
arr = [
    [5, [[0,1],[1,2],[3,4]]],
    [5, [[0,1],[1,2],[2,3],[3,4]]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.countComponents(foo, bar)
print(res)
