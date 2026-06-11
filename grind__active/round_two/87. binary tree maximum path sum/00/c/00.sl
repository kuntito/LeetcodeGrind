i'm given a binary tree.

i want to find the path with the largest sum.

it's a mind bender to consider the different scenarios a max sum can occur.

let's start with the basics.

a leaf node.

a leaf node is it's own max sum.

what if it had a left child?

then the max path sum is either:

* the root node
* the left node
* the sum of them

okay, and it it had a right child?
same thing.

* the root node
* the right node
* the sum of them

what if it had a left and right child.

then it could be..
* the root node
* the left node
* the right node
* the root and left node
* the root and right node
* the root, left and right node.

six branches.
but does it need to be so.

the left and right nodes are their own subtrees
and they have their own response.

but what does that tell me at the root?
ideally, i want to add root + left + right

whatever left concludes is the best max sum at that point,
whatever right concludes is the best max sum at that point,
i want to add it to root.

well, unless, it's negative.
in which case i want to avoid it.

i think this case summarises these three branches.

* the root and left node
* the root and right node
* the root, left and right node.

if i did root and left alone and they're both positive, i'd want to add right, if it is positive too.

i might as well say,
if left is +ve, add to root
if right is +ve, add to root

only reason, i'd do this alone
* the root and left node

is if right is -ve, in which case, my condition handles it.

only reason, i'd do this alone
* the root and right node
is if left is -ve, in which case, my condition handles it.

now, i'm left with these three conditions:

* the root node
* the left node
* the right node

i'd say 
* the root node

is handled by the conditional case.
worst case scenario, both left and right are negative, and so i'm left with root alone.

* the left node
would be the result of the exploration of the left sub tree

* the right node
would be the result of the exploration of the right sub tree.

and so there's only three branches for each sub tree.

* root + max(0, leftRes) + max(0, rightRes)
* leftRes
* rightRes

whichever's largest of all three, is the best max sum at that point
and so we return that.

however, i'm returning two things.

* the max path sum at each subtree
* the better path sum at each subtree

the better path sum answers the question,
starting from root, do i go left or do i go right?

and what would this value be?
ideally you want to add root + leftRes, unless it's negative..
and you'd want to add root + rightRes unless it's negative..

so..

max(
    root + max(0, leftRes),
    root + max(0, rightRes),
)

this would be the better path sum.

feels like a helper function.

actually, you're not checking that leftRes for positive.
you're checking the betterPathFromLeft for positive.
it should be:

max(
    root + max(0, betterPathFromLeft),
    root + max(0, betterPathFromRight),
)

i think the same goes for the first comparisons too..

it should be root + max(0, betterPathFromLeft) + max(0, betterPathFromRight)

reason, it can't be `leftRes` is this could potentially be a span.
from root, we take the better path, left or right.

it works now, but it needs a cleaner rewrite.
also, had to adjust the base case for a null node

from
`
if not root:
    return 0, 0
`

to
`
if not root:
    return float("-inf"), float("-inf")
`

if node is None, you want to return the smallest integer possible.

with `return 0, 0`
imagine the root node was `-1`
the best left sum would be `0`, likewise the right sum.
the comparison would be

the span sum against the best left and best right
and would return `0`

when in reality, the best sum is `-1`