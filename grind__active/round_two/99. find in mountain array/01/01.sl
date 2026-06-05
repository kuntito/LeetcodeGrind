i'm taking an integer and an object, and returning an integer.

the object is called a mountain array.

so, how does this work?

for context, i need to understand what this mountain array is
and how it interacts with the input integer to get the output.

{ the mountain array is an array of numbers with at least three numbers.
and an index, where the values to it's left are progressively smaller
and the values to it's right are progressively smaller. }

the mountain array represents an collection of numbers.
the numbers increase then decrease.

that's why it's called a mountain array.
and by definition, it must have at least three elements.

because a one element collection cannot increase then decrease.
neither can a two element collection, it can only increase, (1 -> 2)
or decrease, (2 -> 1)

so the mountain array needs at least three elements.
i.e. 5 -> 6 -> 4

now, i know what a mountain array is.
well, i understand the concept, but the object.

the object is a wrapper around the array.
i can't access the array directly, i do so using the object method, `get`
i can get the number at an index.

but can't manipulate the array directly.

i can also get the length of the entire array.

now, i want to find the smallest index where...