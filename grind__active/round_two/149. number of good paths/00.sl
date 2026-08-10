there's a graph.

i want to find the number of good paths along it.

it says,
a good path has the same values at the start node
and the end node.


what is this value?

***

i have a graph.

i want to count the number of good paths along it.

a good path has the same values for it's start and end nodes.
and any nodes in-between don't have a greater value.

***

a good path has the same values on it's start and end nodes.

a path, a series of nodes.
the entire graph is a series of nodes.

who are you explaining to?
exactly.

***

i have a graph.

i want to count the number of good paths on it.

a good path has the same value on it's start and end nodes.
the nodes in-between, if any, all have values lower or equal to the terminal nodes.

or you can say,
a good path is one where the terminal values are the same
and no node in the path has a higher value.

okay, and how do i want to find this?
i think i have to explore every node.

each node is a good path.
it's its own start and end node, so same values.
and nothing in-between.

so, for every node,
i'd explore every path,
and keep track if it's a good path or not.

the nodes are unique, their values aren't.
so, i can check- check what.

say you have the nodes

A - B - C

and they all have the same values.
you start, A.
you record A as a good path.
the only place it can go is B.

now, you have A-B, another good path
since both values are the same.

but you never track the good path of B alone.
so, what are you saying?
you'd explore all nodes in one go.

at every node, you're doing two things.

starting an exploration at the node itself.
in this case, that node is the first node.

the second thing, you're doing.
is connecting the current node to the previous.
if they still form a good path, keep exploring.
if not, end that iteration.

i'd need to store the paths to know the uniques.
well, each node has an id, i can concat into a string to know unique nodes.

TODO, start here.
i've created the graph, now to explore every node.