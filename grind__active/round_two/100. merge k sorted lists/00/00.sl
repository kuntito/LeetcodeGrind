i'm given a list.

every item in the list is a linked list.

every of those linked lists is sorted in ascending order.

my job is to return a single linked list.
a combination of all the linked lists and to maintain the ascending order.

what's the approach here?
you want to recursively select the smallest head value.

for every linked list, the question is, which linked list head
has the smallest value.

that forms the start node for the combined linked list.

then repeat the same step.
until you run out of nodes.

okay, but how would i even implement this step?
well, you don't know the smallest head until you see every head.

so at the very least, you'd have to iterate through every linked list to determine the smallest head.

to be fair, i think a min heap could help.

iterate through every node in every linked list.
store their values in the min heap.

construct the combined linked list by forming a `ListNode`
with every element popped from the min heap.

case closed.