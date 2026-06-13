i'm given an array, i want to return a number.

the array contains positive integers.
it's called, `nums`.

what is this number i want to return?

it's called `minimum deviation`.
and what does that mean?

we'd need some context.

***

you can perform two types of operations on any element of the array any number of times:

if the element is even, divide it by 2.
if the element is odd, multiply by 2.

the deviation of the array is the max difference between

***
are the operations exhaustive?
it seems like i could go on for ever.

what would make me stop to know i've explored all array configurations?
you want to close the gap.
so, the question is, what numbers in the array can you keep reducing.
what numbers can you keep increasing.
and at each step, you take the difference between the array's lowest and the array's highest.
this figure, ideally, should be decreasing, the moment it increases, you know you've hit your limit.
further iterations wouldn't do you any good.
is this right, well, i'd write it and find out.

***
let's apply the algo to this
[4, 1, 5, 20, 3]

i'd get the deviation as is, 20 - 1, i'd have nineteen.

i can either increase the smaller one or decrease the bigger one.
right?
wrong.

increase or decrease isn't dependent on which is bigger.
it's dependent on parity.

so at each point, i have two moves.
i have at most two moves.
if both numbers are odd?

no..
`
you get the deviation of the array.
then, you try to find a smaller deviation.

that's the core.
you repeat this step until, there's no greater deviation.
`

TODO...continue this.