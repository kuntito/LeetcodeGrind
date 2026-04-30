# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

what's the situation?

i have an array of integers.

i want to find out the integer with the largest reach.

an integer's reach is defined by how far it can travel in both directions, left and right.
in each direction, it's checking for the same thing.

how far can i travel in this direction before finding a number less than me.
once, you have both values.

the reach is defined by the formula, 
`totalSteps times number`.

totalSteps is defined as leftReachCount + rightReachCount + 1.

my first attempt at this was to travel left and travel right for each integer.
but it was deemed inefficient.

why's it inefficient, well because, i'm travelling the same direction multiple times for different numbers.

well, each number is different.
so each travel isn't seeking the same thing.

but the fact that i've travelled before.
can it tell me something?

for each number, i want to know how far i can travel left or travel right.
but how does one number's travel allow another to find it's result easily.

consider

[2, 2, 1]

when i explore `2`, i'd can take one step right.
there's no step at the left.

so i'd have 2, 2

now when i hit `1`
what's the challenge, i want to go left and right.
i can't go right, no more numbers.

so i go left.
but before going left.
i know i've explored the number before.

what's the prior number, it's a `2` with a streak of `2`
now, i know i'm less than `2`

and so any of `2`s streaks is automatically valid for me.

what if i'm higher than `2` i.e. [2, 2, 3]
it would mean none of 2s streaks is relevant to me?

is that so?
if you had [2, 2, 3]


actually, i'm not looking at this right.
for [2, 2, 3]

for the first `2`, i can only travel rightwards.
and so, i encounter another `2` and the exploration stops there.

now, i'm at the second `2`
the fact here is, if the numbers are equal and next to each other.
whatever the first `2` found is what the second `2` will find, no need for exploration.

then we move to `3`
now, three looks back, it's a `2`
you can't use anything from `2` since it's less

so the only way is to explore rightwards.

now, what if it was `2, 2, 1`
at `1`, i'd look behind and see something bigger.
the conclusion is, whatever that guys streak is, leftwards, is also my streak at this point.

so all that's left is to check forward.
it's become obvious, that i can always know how many consecutive items have come before.

looking back, there's only three options.

same number
lesser number
higher number

same number means same streak, you can continue iteration.
lesser number means, no left streak.
higher number, means, same left streak

and how does this help me solve anything?
