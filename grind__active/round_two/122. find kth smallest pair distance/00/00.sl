i'd take an array and return an integer.

what is this integer?

it's the kth smallest pair distance.

that doesn't help much.

let's add context.

the array contains numbers.

the numbers can be picked in pairs.

every pair has a property, `distance`

`distance` is the absolute difference between
the two numbers that make up the pair.

now, if we ordered the pairs, what would be the kth pair?

take that pair and return it's `distance`.

that's the question.

okay, so.. the solution lies in the order of pairs.

how are these pairs ordered?

the pair is two numbers.

the pattern is you hold the first number,
then determine pairs, by iterating through the rest of the array.

if our array was
[5, 3, 2]

the first pair would start with the first number in the array.

`5`

once, we have this, 
we iterate through the rest of the array to get the different pairs

i.e.
(5, 3)
(5, 2)


we've exhausted the array.
so, at this point we pick a different first number.

`3`, and it's only pair is (3, 2)

when ordered, the pairs are..

(5, 3)
(5, 2)
(3, 2)

and so, we can get k=1, k=2 or k=3.

there's probably an efficient way to determine the kth pair
than listing out the pairs but i'd start with this.

then improve.
