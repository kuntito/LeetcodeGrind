i have graph.

like all graphs, it has edges.

i care about two kinds.

ones where removing them from the graph
increase some property of the graph.

and other ones that don't necessarily increase
the same property of the graph when removed.

so, the property is leading the discussion.

what is this property?
it's called minimum spanning tree.

it's a subset of the graph,
without any cycles
and with all the nodes intact.

so, really, an MST is what you get after removing
some edges.

you want to keep the graph nodes connected.
without any cycles.
and the lowest edge weight.

what is this edge weight?
a property of the line that connects two nodes.

perhaps, this'd be simpler.
if i properly defined a graph.

a graph is a connection of things.
where each thing can tell you what it's connected too.
human relationships is a good example.

i know paul, i know james.
that's a graph.

i'm connected to paul.
i'm connected to james.

that connection, is what's called an edge.
in CS, it's represented as a line between
me and paul, and another line between me and james.

usually, the direction of the line matters.
if i know paul and paul doesn't know me.
then the connection between us is one way, unidirectional.

if i know paul, and paul knows me.
the connection is bidirectional.

in this case, we're dealing with bidirectional connections.
bidirectional edges if you will.

now, that i have a better sense of a graph.
let's fill up the picture.

say, i have a graph.
a network of friends.

we're all connected in one way or another.
paul has his connections, i have mine.
and since i have access to paul,
i have access to his connections.

and he, me.
now, all connections are not equal.
some are more expensive than others.

me, maintaining a connection to paul
might cost me late nights, maybe even money,
since, it typically involves going out to expensive places.

now, getting a minimum spanning tree
is saying, what's the cheapest way
i can keep all connections cheap.

not just with paul, but the overall network.
how can everybody still know everybody
without spending so much money.

sometimes, the network is already efficient.
you really can't get cheaper than that.

but in our case, we don't know
so would have to find out.

but particularly, what i want to know is.
what are the connections i can't break?

and what are the connections that i can.

so, what would make a connection unbreakable.
well, if it's the cheapest way to keep two
people connected, you can't touch it.

long shot, but it seems to me like you'd start with
the cheapest connections first.

every connection is treated as critical, until
you find a way to connect the same node
at the same price.

at which point, you move the connection to pseudo critical.
lemme write it and see.