i'm given two things.

the head of a linked list.
and an integer, `k`.

what i want is to reverse the nodes within the linked list.
k nodes at a time.

say the linked list has five nodes and k is `2`
1->2->3->4->5

* i'd reverse the first two nodes (1->2)
it becomes (2->1)

now the entire linked list looks like
2->1->3->4->5

* next, i'd reverse the next two nodes (3->4)
it becomes (4->3)

now, the entire linked list looks like:
2->1->4->3->5

* next, i'd reverse the next two nodes (5->?)
there is no next two nodes.

at this point, the question dictates i leave those nodes as they are.

it's basically a sliding window of size `k`
where i reverse the order of nodes.

if the last window isn't size `k`, i'd leave it as is.

so two problems:
* how am i moving the window?
* how am i reversing?

***
to represent the window, i'd use a counter, `i`
i'd increment `i` as i move through the linked list.

at some point `i` becomes a multiple of `k`
so i know i can reverse every
***
to represent the window, i need to know where it starts and where it ends.

if i use a counter, i can tell where the window ends.
but not where it starts.

how about a variable, `nodeStart`
it's initialized as the head of the linked list.

i iterate through the linked list.
incrementing the counter `i` on every turn.

the moment `i` becomes a multiple of `k`
i know i've hit the end of that window.

using my reference to `nodeStart`, which is better named, `windowStart`

i can reverse the window.
once i reverse the window.

i attach the tail of the reversed window.
which would be `windowStart`

i'd attach this tail to the next node.
once attached, that next node becomes the next `windowStart`
and i'd repeat.

all said and done, how do i get a reference to the head of the new linked list.

consider this, ll is 
`1->2`

and `k` is `2`

windowStart = 1
when i iterate to node 2, i becomes 2
2 is a multiple of k,
so i reverse the window.

the window becomes 2->1
i attach the tail, `1`, to the next node, None in this case.

but how do i know to return `2` as the new head?

a better approach might be to track the node before the window start.

in this case, i'd create a dummy node and point to the linked list head.

so, from the jump, i'd have:

dummyNode -> 1 -> 2

does the window start logic still hold?

***
start here,

you want to iterate through a linked list with a sliding window of size k.

k is guaranteed to not exceed the number of nodes in the linked list.

on each k-window, you want to reverse the order of nodes.

if the last window does not have k-nodes, leave as is.

when done, return the head of the modified linked list.

one thing i learned is, 
i can set the first node to `windowStart`
then track how many nodes i've seen as i iterate.

when i see k-nodes, i know i can start a reversal from `windowStart`

however, the problem is, after reversing the window.
how do i attach the new head to what came before?

for example, ll is `1->2` and k is `2`

in this case, the entire ll is the window.
when i reverse this, i'd get `2->1`

but how do i know to return `2` as the head of the modified ll?

rather than note the window start, i'd note the node before the window start.

i'd use a dummyNode for starters.

dummyNode->1->2

this way, i can count every node after it, to know when i reach the window end.

i'd reverse, re-attach, update pointers accordingly.

