i misread the question the first time.

i have an array and want to return a number.

what is this number?

the number is the kth smallest pair distance.

but what does this mean?

let's add context.

the array contains numbers.

these numbers can be picked in distinct pairs.

and each pair has a property, `distance`

a pairs `distance` is the absolute difference
between the two numbers that make up the pair.

my job is to find the kth smallest absolute difference.

to do this, i'd have to know all the pairs?

well, that's the basic idea.

get all the pairs.

sort them by distance.

pick the kth one.

let's start with this.

how would the sorting go?

i'd say a max heap of size `k`

this way the number at the top is always the kth smallest distance.

