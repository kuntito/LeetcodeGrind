i'm given a binary tree.

i want to represent it as a string.

such that the string retains enough information that i can convert it back to the same binary tree.
***

a binary tree is a group of items. 
and each item can have at most `2` children.

each child is also an item.
and so, they can have at most `2` children.

it's recursive in nature.
and the end case, is an item with no children.

a sample representation is:

 1
2 3

the first item is `1`
and it has two children, `2` and `3`

both `2` and `3` are also items, but they have no children.

the typical name for these items is node.

the first item is called the `root node`
the items without children, are called `leaf node`

***
okay, so how would i represent this as a string.
well, i can start with the root node.

i'd store the value.
now what?

i'd check it's children.

say the left child.

on explorting the left node.
i'd realize, i'm at the same point where i started.

i have a root node, with children.
so, i'd store this left node too.

my store would contain [1, 2]

then what?
i'd explort the left child of the left node.

this is recursion.

with every node, i'd store it.
then explore it's left child.

at some point, i'd find there's no left child.
then what do i do?

explore the right child.

and where am i storing all these items?
i could use an array.

for the sample case:

 1
2 3

my array would be [1, 2, 3]

i can then convert this to a string, by concatenating each item with a separator.

i.e. "1-2-3"

okay, but how would i convert this back into the same binary tree?

for one, i'd know "1" is the root node.

then i'd be at "2", is two the left node? well, it is.
but i only know that because i know what the binary tree used to look like.

in reality, it could be the right node.
why would it be the right node?

consider:

 1
  2
   3

this is still a binary tree.
the root node is `1`

it has no left child, so it explores the right child, `2`
you store `2` as is the practice.

then explore it's left child.

it also has None.
so it explores the right child.

`3`, stores it too.

you'd realize at the end of this exploration.
you'd have an array [1, 2, 3] which converts to "1-2-3"

as far as we're concerned, 
the string tells us nothing about the shape of the binary tree.

just that the root node is `1`
and it has two other nodes.

we need a way to distinguish, left nodes from right nodes.