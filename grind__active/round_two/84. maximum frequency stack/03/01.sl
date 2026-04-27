i want to implement a data structure.

what does it do?

it stores elements and can remove stored elements.

`the elements are integers and they are stored in the order they arrive.`

if an element already exists in the structure, 
adding another copy stacks the new copy on the old one.

for instance, your structure contains the elements:

4 1 3

and you want to add another `4`, the stacking becomes:

4
4 1 3

and now, the removal.

`right to left, the structure removes one element from the tallest stack.
it returns that element.`

and how would this work in code?

*
a `stack` naturally stores elements in the order they arrive.
i can note the indices for each element in a `hashmap`

that way, i've stored the elements in order and can access the order in O(1) time.

and the removal?
i'm thinking heap for frequency?

well, not just frequency.
frequency and recency.

Python naturally handles that. `(negIdx, freq, element)`
this way the element we want is always on top of the heap.

once, removed.
+   update the hashmap
+   remove element from `stack`, now that i think of it. i don't need the stack.

the `hashmap` let's me know what elements i've stored.
the `maxHeap` let's me know the recency.

every new element is given a `recency`.

the heap naturally handles the removal.
once, removed.
+   update the hashmap
        reduce the element frequency.
        if frequency becomes `zero`, remove it from the hashmap.

i think that's it.
every new element is added to the maxHeap.
what if it's an existing element?

well, we need (recency, freq, element)

if it's an old element, we know how to get freq.
from the hashmap.

in that case, the hashmap should also store recency.

* hashmap: elem => (freq, recency)
* maxHeap: (recency, freq, elem)


*** didn't work.
run the code in d.py to see breaking test case.

one error i observed and fixed was the maxHeap items.

i'd stored (recency, freq, elem)
which sorts by recency first.

but should sort by frequency first.
then recency.

so: (freq, recency, elem)


FAILING TEST CASE:
["FreqStack","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]

[[],[1],[0],[0],[1],[5],[4],[1],[5],[1],[6],[],[],[],[],[],[],[],[],[],[]]


TODO: also, it seems recency should only be updated when we add a new element.

TODO:
it seems i've misunderstood the structure.

the elements don't necessarily stack.

i note their frequency, but each copy of the same element has a differenct recency.

i'd previously used the same recency for all elements of the same type.

till next time.

turns out, i fixed it.
each heap element should contain the current recency.


i've muddled up my thought process,
the code needs a rewrite.

i didn't need to store recency in the hashmap.