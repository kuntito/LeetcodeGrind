three inputs, one output.

the inputs are one integer
and two arrays of numbers.

both arrays are sorted.

now, let's define a pair as two numbers, one from each array.
when the numbers in a pair are multiplied, a product is formed.

if you took every pair, and lined up their products in ascending order,
what product would be in the kth position?

***
well, i'd have to take every pair and multiply then sort
to know the kth smallest one.

i could do an n2 iteration, keep products in a max heap of size `k`
so the number at the heap top is the result.

`seems like it's the same problem as 'kth smallest pair distance'`