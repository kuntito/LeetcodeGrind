i have a linked list.

i want to reverse it's nodes in batches.

all batches are the same size.

i'd reverse the first batch
then reverse the next batch
and the one after that until i reach the end of the list. 

if at the end, i don't have enough to form a batch.
i leave those nodes as is.

the batch size is `k`


***

now, what's the approach?

run through each batch
reverse it, keep it connected to the next node
till you reach the end.

and how would you capture each batch?
you count the nodes.

and when you reach node k, you reverse.
reversing demands you know the first node in the batch.

so, two pointers?
one at the start, another that counts and stops at node k
with this i can reverse.

now, how do i connect?
take the new tail and point it to the next node

it's best i write the code.
