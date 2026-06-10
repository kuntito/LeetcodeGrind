i'm given a string.
i want to return a binary tree.

the string represents the pre-order traversal of the binary tree.
i want to work backwards to create the binary tree.

what's pre order traversal?
it's a way of exploring all the nodes in a binary tree.

you start with the first node, root.
then check it's left node..

if that has a left, you check it's left.

you keep checking left till there's nothing left.

***

a binary tree is a network of nodes.

it starts with one node,
it's generally called `root`.

***
TODO i couldn't figure this out.
i'm trying to define pre-order traversal in relation to the question.
the string given, is a pre-order traversal of the tree
each node is a number
and is preceeded by zero or more dashes.
the dashes tell how deep the node is,
in the binary tree.

the root node is one level deep.
it's children are two levels deep.

so

 1
2 3

is represented as `1-2-3`, i think...
i think because i didn't read the question till the end.