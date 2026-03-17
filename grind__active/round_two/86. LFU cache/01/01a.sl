i want to implement a data structure.

it stores key value pairs.

it provides two methods, `get` and `put`.

`put` takes two arguments, the key and the value.

`get` takes one argument, the key, and returns it's value.
if there's no value associated with that key, it returns -1.

the data structure also has a max capacity.
once it's reached, it has to delete an entry to make room for a new one.

the entry removed is the least frequently and least recently used key.

**

how would the code work?
well, first what determines frequency and recency of a key?

frequency increments whenever you get or put a key.

recency is when last you put or get a key.

a frequency map solves the frequency problem.
a recency map solves the recency problem.

how do you solve the O(1) removal?

a min heap could work.

each heap item is
(freq, recency, itemKey)

so four structures?

a map of key => value
a map of key => recency
a map of key => frequency
a min heap of (freq, recency, itemKey)

the top of the min heap is always what we'd remove, if at capacity.

every time you get or put, you add an entry to the heap.