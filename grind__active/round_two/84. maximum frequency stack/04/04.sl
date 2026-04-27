# https://leetcode.com/problems/maximum-frequency-stack/

i want to design a data structure that stores elements based on the descending order of their frequency.

***

i want to design a structure that stores integers
and maintains a descending order of their frequency.

***

i want to write a class that stores integers.
it can take an integer.
it can release an integer.

however, it always releases the integer with highest frequency and most recently added.

***

i want to design a data structure.

it stores integers.

***
i want to design a data structure that allows you store integers.

and let's you retrieve the most frequent and most recently stored integer.

okay, how would the storage work?

a heap lends itself nicely to this problem.

a max heap.

it allows me store the integers.

you can store the integers, but that's not what you want is it.

you want to store frequency.

but frequency is paired with the integer.

so your maxHeap item is looking like (freq, number)

and what would it look like if you add a number once.

what goes in the max heap?

say the number is `1`

your first entry is (1, 1)

and what happens when you add another `1`

the entry becomes (2, 1)

how did i get two?
well, i know i already added `1`.
so another `1` takes the frequency to `2`.

i can use a hashmap to track frequency.

this way, i can always generate the heap item.

okay, the heap tracks frequency, but i also want to track recency.

the item at the top of the heap, should be the most frequent and most recent number.

in which case, my heap item should be (freq, recency, number)

if there's a tie with the frequency, the max heap automatically sorts by recency.

so the top of the max heap is always what i want to remove.

and when i remove a value, the heap re-heapifies,
restoring the new most frequent and most recent number to the top.

and i'd remember to update the hash map too.
