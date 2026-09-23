there's a graph.

it has three kind of edges.

type a,
type b, and
type ab

there are two people.
Alice, and Bob.

they can go anywhere on the graph.
as long as they follow the right edges.

Alice can only follow edges:
    type a, and, type ab

Bob can only follow edges:
    type b, and type ab

i want to return the max number of edges
i can take out the graph
that still allows both Alice and Bob go anywhere on the graph.

and if it was never possible for both Alice and Bob to go anywhere
then, i'd return -1.

okay, so how do i approach this?
first, see if both alice and bob can explore the graph
rule of the -1.

then recursively remove every edge.
elaborate.

you have `k` edges.

remove one.
see if both can still traverse.
if yes, remove another one.
and keep going till the point you can no longer remove.

track the quantity removed.
go back up.

so what's the pattern.

you'd start:
    can both alice and bob explore?
    if no, return -1.

    if yes.
        explore every edge.
        at each one,
            explore what happens if it wasn't there.
            that's essentially repeating the entire scope.

    and what happens when you're done exploring every edge?
    {
        say you're at the leanest graph.
        it would mean, removing every edge and exploring
        would give you -1.

        in which case you can't remove any one.
        so, you can return 0.

        and what would have happened if at least one edge could be returned.
        that branch would have explored the remaining edges and seen it could do nothing.

        TODO start here,
            would need to model on paper what the recursive approach looks like.
            base-case, and pre base-case
    }