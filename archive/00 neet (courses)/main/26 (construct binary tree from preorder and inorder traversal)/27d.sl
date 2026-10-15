# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

i have two arrays.

each represent an order of nodes in a binary tree.
both orders are different.

***

i have two arrays.
they're similar.

they contain numbers.
and those numbers represent the 
nodes on a binary tree.

each array contains method to ordering the numbers of the binary tree.

given these two numbers,
i'm supposed to figure out what the binary tree looked like.

the assumption is, these two arrays contain enough information.

that assumption is true.
i know, because, i've solved it before.
but even i hadn't.

how would this have gone?
well, i'd have to understand what each order, each array says about the binary tree.

the first order, is called preorder.
and it starts with the root node.
then the left node, or rather the left subtree.
what does this mean?

it means, treat the left node as it's own root node.
and what would that mean.

take the left node, and it's left subtree.
it's recursive.

you'd basically keep taking left nodes.
till there's no more.

at which point, you take a right node.
and move up the subtree.

the logic kinda writes itself.
just pick root, pick left tree, then right tree.
and eventually, you run out of nodes.

okay, what does this tell us?
well, it means, for each root,

all the nodes in it's left subtree
and it's right subtree are explored after it.

and in particular, the nodes entire left subtree
is explored before it's entire right subtree.

and so? doesn't this give us a binary tree?
i know the root, i know the nodes after it
are it's left subtree.

well, i don't know that.
a node without a left subtree
and one with one, can look identical as arrays.

consider
[1, 2, 3] where the tree is
 1
2 3

and, [1, 2, 3] where the tree is
 1
   3
  2

these are two different trees.
and the array doesn't tell them apart.

perhaps, that's what the second order does.
elaborate.

it's called a inorder.
and it takes a different direction.
it explores the entire left subtree first.
then the root.
then the entire right subtree.

i think this helps us.
this helps me.

preorder traversal, tells me the root
and the left subtree and right subtree are after it.

inorder tells me the left subtree
is before the root, and the right subtree is after the root.

this way, if i take the entire array after root.
take the first half,
and compare it with what comes before the root in `inorder`
i can know where the left subtree ends
and where the right begins.

the solution writes itself.
every array is it's own tree.

recursively explore till you have your binary tree.

let's illustrate with these two trees.
 1
2 3


 1
   3
  2

their inorders are respectively
[2, 1, 3] and [1, 3, 2]


and so, if i start my deduction from the preorders.
[1, 2, 3] and [1, 2, 3]

i can work my way back to the tree.
let's explore in pairs.

first:
[2, 1, 3], and
[1, 2, 3]

i'll start with the preorder.
the root is `1`

then i know [2, 3] represent the left subtree and right subtree.
if i find `1` in the inorder, `[2, 1, 3]`.
i know, everything on it's left is the left subtree.
in our case, `2`

so, i know my left subtree.
and the right subtree is everything after the root.

in essence, i have the tree.
root
left subtree, and right subtree.

this is the most basic case,
what if it wasn't basic.

well, the fact is, you can start like this.
root, left + right
left, root, right

then i'll run the same program.
with the first left, and the second left.

it's the preorder and reorder.
i'll keep going till i hit the base case and voila.

can i write this?
let me try.

BTW, all values in the array are unique.
without that, it'd have been hard to tell which number is root.