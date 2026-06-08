i want to merge linked lists.

how?

the linked lists contain integer nodes,
nodes sorted in ascending order.

and how would the merge go?

throw all the nodes in a min heap.

pull out each node and construct the merged heap.

can i do this?

let's find out.

it worked with a tweak.

to store nodes in the heap, i used a tuple of three elements.

`(node's integer, an item count, the node object)`

the min heap heapifies based on the node's integer
and if there's a clash, item count is guaranteed to be unique
so, the heap pop works as planned.


***
now, i've written it.
what's the next step?

see if it can be written better.
first, what's the run time complexity?

i put all the items in a heap, i think that's log n for each item.
so nlogn for adding all items to heap.

i iterate through every linked list node, that's O(mn)
where m is the number of linked lists, 
and n is the number of nodes in each linked list

then i popped from the min heap
log n for each pop, and so, nlogn

in summary,

O(mn) for iterating all nodes
nlogn for insertion
nlogn for removal

TODO verify the run time assessment is correct.
do space time complexity.

the algo merges linked lists with integer values
into one big linked list, where the integers are sorted
