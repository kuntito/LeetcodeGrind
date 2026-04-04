# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/

i'm given the edges of a graph.

i want to find critical and pseudo-critical edges in the minimum spanning tree
within the graph.

this is a mouthful, if i'm being honest.
but let's break it down.

first, what's a graph in this context.
a connection of nodes.

what's a node.
think of it as a circle with a number inside.

i think the idea behind this, is a graph is a way to represent
a connection of multiple things.

in this case, we have a graph of numbers.
we can have a graph of anything.

it's a graph because you have several things connected to each other.
in this case, several numbers connected to each other.

the terminology for the things being connected is nodes.
so, the a graph has nodes, a node is a point on a graph.
they kinda need each other to be defined.

now, we have a graph of numbers, and are given edges.
what's an edge?

the connection between the two numbers on a graph.
a connection?

well, when you draw it out, it's simply a line.

1 --- 2

here, you have an edge between the numbers (nodes)
`1` and `2`

the question uses the term, undirected, this talks about the direction of the edge.
if i've never dealt with graphs before, this distinction wouldn't matter.

but for context sake, undirected simply means
i can travel in both directions on the edge


i can go from `1` to `2`, and
i can go from `2` to `1`



a directed edge would look like this,
1 ---> 2, OR
1 <--- 2

meaning i can only go in one direction.

another thing the question mentions is "weighted"
a weight is simply a number assigned to an edge.

think of an edge as 

TODO
* define a graph, talk
    nodes
    edges
    weights
    undirected
* define MST
* define Critical and Pseudo-Critical edges