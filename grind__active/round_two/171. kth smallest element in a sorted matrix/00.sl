i have a grid of numbers.

all sorted left to right.
the rows, i mean.

an example is:

1, 2, 3
4, 5, 6

i want to find the kth smallest number in the grid.
without doing O(n2)

in essence, how can you solve this without traversing the entire grid.

well, you need to traverse the entire grid.
do you not.

is that even O(n2)?
yeah, it is.

that's exactly it.
so, how can we be efficient.

can you know the kth smallest number in the grid.
well, for a start the kth number tells us that we can 
safely ignore every number before the kth number in the grid.

and from there what?
actually, you can't ignore every number before the kth one in the grid.

reason being, you need to know the contents of those numbers.
so you can tell if it's the kth smallest number.

i don't see a way around O(n2)
you need to at least see the numbers in the grid
to know what the kth smallest one would be.

well, the kth smallest number is asking
for the kth number in the grid.

say, you lined up the numbers.
give me the kth one.

oh, that's simpler.

with k, i can calulate what row it should be, then iterate on that row to find the value.

and how would it go.

k is asking the number of items before i get to target.

if i mod k by the length of each row.

actually it's a div mod.

if each row has 5 items.

and k is 6.

it tells me my answer is `divmod(k, 5)`
which would give me `1` and `1`
so 1 row passes and the first element on the second row.

actually no.

the grid guarantees each row is sorted.
not that the last item in each row

is smaller than or equal to the first item on the next row.

[
    [1, 2],
    [1, 2]
]

is a valid grid.

in which case, my divmod fails.
i really don't see how.


not sure what to do, i'd attempt this question with a fresher mind.