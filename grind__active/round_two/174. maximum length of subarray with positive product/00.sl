i have a queue of numbers.

i want to find the longest stretch
in the queue where the numbers form a positive product.

well, the stretch has to start somewhere.

to be fair, find the longest streak without a zero
or an even number of negative numbers.

since, the zero strikes out the others.
and an odd number of negatives mean
you can't get a positive product.

how about:

[1, -3, 2, 3, 4]

i've got a rough draft of this.
for one, i'm only concerned with non-zero streaks.

my answer must be within those.
say, i have a non-zero streak

what do i care about?
negatives.

if i have no negatives or an even number of negatives
then the streak is up for consideration.

if i have an odd number of negatives.
my idea, is i only need to care about the first negative.

then count the numbers on it's left.
and the numbers on the right.

whichever is larger.

so, find a non-zero streak.
track what you're seeing so far.

and at the end, if odd negatives.
compare the longer side of the first negative
to what you have so far.

