# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
from typing import List

# i'm given two things.

# an integer `n`
# and a 2d array of integers, `edges`

# let's break this down a bit, it's a graph problem.

# `n` refers to the number of points on the graph.
# each element of `edges` is three things.. 
# [a point, another point, the weight between the two points]

# when this graph is drawn out, something exists, called minimum
# spanning tree, MST.

# this is a path that connects all points on the graph
# with the lowest total weights possible.

# say you have a graph:

# a <-5-> b <-2-> c <-1-> a

# not the best of diagrams
# but `a` is connected to `b` with weight `5`
# `b` is connected to `c` with weight `2`, and
# `c` is connected to `a` with weight `1`

# all three points have a cyclic connection.
# but the shortest paths connecting these two is:
# `b` through `c` to `a`
# a total weight of `3`

# going the other way, b -> a -> c
# would be a total weight of `6` points.

# so now, that we have the intuition of MST
# what are we doing with it?

# i want to find and return all critical and pseudo-critical edges
# in the graph.

# what are these things, let's start one after the other.

# first, what's a critical edge?
# and edge when removed increases the total weight of the MST.

# okay, this suggests that there can be multiple MSTs.
# i mean our example above revealed two.

# b -> c -> a results in 3
# b -> a -> c results in 6

# but what's the critical edge in this case?
# b -> c -> a has the weights 1 + 2
# 
# b -> a -> c has the weights 5 + 1

# if you remove an edge from an MST
# it stops being an MST..

# the question is wrong. at least the way it's phrased.
# i think what it's saying is, if you remove a critical edge..
# and form an MST with whatever points are left
# the new MST would have the a greater total weight

# verbatim it says... `Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge.`

# i think i misunderstood it.
# what it's saying, you have a graph, find the MST.

# every graph, in this question, has an MST. i'm assuming this.
# i'll find out if i'm wrong.

# every graph has an MST and by extension an MST weight.
# MST weight is the total of all edge weights in that MST.

# what the question is saying is, if you remove an MST edge from the graph.
# one of two things can happen:

# a new MST is formed.. OR
# there's no new edge that can form an MST.

# say you had a -> b -> c
# the graph is it's own MST

# removing any edge doesn't result in a new MST.

# so what does this mean? the question doesn't say what happens.
# am i to just class the edge as critical?

# yes.

# Claude has made it clear i should work within the constraints of the question.
# there's two realizations here:

# one, i thought removing an edge from a -> b -> c causes no MST.
# then second, i realized, the MST has now become whatever's left..

# seems i was seeing too clearly..
# i don't think i was wrong the question wording doesn't accomodate this situation.

# right, so i'd redefine the critical edge.
# an edge that when removed causes the MST weight to increase OR 
# reduces the number of nodes in the MST.

# the first case is simple to understand in a cyclic loop.
# a <-> b < -> c
# you have two MSTs a -> b -> c and b -> c -> a
# remove an edge from one, you can form an MST with the other.

# the second case is for an acyclic graph.
# a -> b -> c

# in this case, the MST is the graph.
# removing any edge would mean removing a node along with it.

# effectively shortening the MST to one less node.
# it's an edge case, i guess. if there is only on MST, every node is critical.

# i can probably shortcircuit from this.
# if len(edges) == n - 1, return edges.

class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:
        pass