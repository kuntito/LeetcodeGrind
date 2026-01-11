# https://leetcode.com/problems/tree-diameter/description/

from collections import defaultdict
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        pass
        # we're given a tree and want to find it's diameter,
        # the diameter is defined as the longest path in the tree
        # the path isn't necessarily root-> leaf
        
        # the path is leftLeaf -> root -> rightLeaf
        
        # we'd have to employ a recursive approach where we monitor the path
        # at each node
        
        # for each node, we want to know how many left nodes and how many right nodes
        # the sum of these is the path at that node
        # we declare a global variable `maxPath`
        # that's updated at every node and c'est finni
        
        # well, not really we have edges and not a tree
        # so we'd have to create the tree then explore it
        
        # this presents a unique problem since we don't know the root of the tree
        # how do we find the root, the root is the one node that has no parent
        # we know all nodes are labelled 0 -> n-1
        
        # we'd create a set of node values
        # and remove from the set any node that has a parent
        
        # but we'd tweak our approach a bit
        # the tree is not binary tree, so we aren't adding left and right
        # we're adding the top two depths
        
        n = len(edges) + 1
        allNodes = set(range(n))
        
        graph = self.createGraph(edges, allNodes)
        
    def createGraph(self, edges, allNodes):
        graph = defaultdict(list)
        for uno, dos in edges:
            graph[uno].add(dos)
            allNodes.remove(dos)
            
        # i seem to have made a mistake, the nodes are undirected
        # meaning the paths are both ways
        # in that case, how do you find the root?
        
        # i'd say create a graph
        # run dfs on every node, store the longest path found