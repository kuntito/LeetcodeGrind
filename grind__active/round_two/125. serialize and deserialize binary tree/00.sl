i have a binary tree.
i want to represent it as a string.

the string should contain enough information
that i can rebuild the binary tree.

and how would this work?

how do you describe a node?
it's described in relation to other nodes.

leaf nodes are the simplest.

a root node has children.

a node has children.

i think this is the simplest it gets.

you want a relationship between a node and it's children.

a node, has two children.
left and right.

each child has it's own children.

it's recursive.

and the base case, is the node with no children.

the leaf node.

so start with the leaves.

and work your way up.

once you find your first leaf,
what more do you need?

you need to know it's parent.

* know the leaf
* know the parent

once, you know the parent what next?
* know the second leaf

the parent has two kids
two leaf nodes.
you need to know both nodes.

and for each leaf node.
you need to know it's parent.

it's also recursive.

starting at root, you explore it's leaf nodes.
no.

starting at root, what do you want?

you want to know it's kids.
and so, you check the left child.

this is the recursive step.
at this point, the left child becomes the root.

and so, you want to know it's kids
so, you check it's left child.

it has none.

then what?, well one kid is missing.
on to the next.

you check it's right child.
it has none.
now, what?

this node has no kids.
it's a leaf node.

you keep track of it.

now, it's parent, `1`
what are we saying.

we know it's left kid, `2`
we've stored it.

we need to know it's right kid.
we check the right node.

now, this node becomes the root.
at root, we want to know the kids.
starting with the left.

and so, we check, `4`
now becomes the root.
at root, we want to know the kids
starting with the left

but there is no left.
so a kid is missing.
we check for the next.

there is none.
this node has no kids.
it's a leaf node.

we track it.
now, what?

we check it's parent, `3`
we found the left kid and stored it.
now the right kid.

we get to 5,
it becomes root
no left, no right.
it's a leaf node.

we'd store it too.

then return to parent, `3`
we have both kids, 4 and 5.

now, we establish a relationship.
`three's kids are 4 and 5`

now we go to 3's parent, `1`
1s right kid is 3.
1s left kid is 2.

that's all 1 needs to know.

3 needs to know it's left and right kid.
that's the core.

each parent should know it's kids.
now, how can i express this as a string.

in this case, i'd want to start with 3.
it has two kids, two kids without kids.

so, i do 3,4,5

i know three is the node
four is the left kid
five is the right kid.

now, i introduce one.
one has two kids.

two and three.

if i do the same thing.
1,2,3,4,5
i can say 1s kids are 2 and 3

i can say 3s kids are 4 and 5

but this makes sense to me because i can see the graph.
what if 2 had kids.
what would this look like?

perhaps, i could use parentheses.
the parent outside, inside the parentheses
two entities.

left and right kid.
if either is missing, leave empty.
 
it's like each number is outside a two element tuple.


so 3(4, 5)
then 1(2(,),3(4, 5))

so this way, it's clearer.
1 has two kids.

2 and 3
2 has no kids. hence, (,)
3 has two kids. hence (4,5)

actually, 4 and 5 are nodes.
so they should be, 4(,) and 5(,)

the more accurate representation is:
1(2(,),3(4(,),5(,)))

it could grow messy to look at
but i'd say it maps the problem well.

i'd continue from here TODO