i have a grid of 0s and 1s.

i want to find the largest connecting group of 1s
assuming i can change any 0 to a 1 to aid my cause.

but only one 0.

so, how would you do this?

take each row, and see how far down it grows.

for each row, you want to keep a streak of 1s.

if you have `1110111`
you'd have two streaks of 1s.

the question is, how do you know if it's favorable to use your zero here.

or pick each streak
and use the zero downwards?

it's feeling like both.
find the streak `111`

explore downwards
still with the possibility of changing a 0 to a 1.

it feels like there's three decisions when you hit a zero.

one, take your streak.
explore downwards.

fill the hole and continue the streak.

the third, i'm thinking
when you don't use a zero
how do you find any streaks after the zero.

yeah, the operation,
is traverse a row.

and track a streak.
you keep going.
till you hit a zero.

at which point you do three things.

one is you explore the streak downwards, hold your 0 intact.
two is you fill the gap, continue till it ends, explore downwards without 0 intact.
three, is, start another iteration with idx + 2

it's a explore left to right
explore downwards.