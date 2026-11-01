https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/description/?envType=problem-list-v2&envId=0ruz2bq5

i have a queue of numbers.

i want to find the longest.

no.

i have a queue of people.

i want to find the longest line
i can form where their heights don't increase.

and return the number of people in said line.

now, the line doesn't have to be back to back.
i can pick the first person then the third person
if that gives me a longer queue.

for instance,
if the heights were

352

well, for this, `32` and `52` actually work.
so really, how would i model this?

well, from the beginning.
with the person with height `3`
they're the only ones i can pick.

when i introduce another person.
now, i have to make a decision.

does the person join this queue
or start their own.

since i have 35

they can't join the queue.
since 5 increases the queue height.

5 forms it's own queue.

then comes 2.

2 can join 5s queue
or join 3s queue.

how to decide.

if i join 3, i'd need numbers 3 or less moving forward.
if i join 5, i'd need numbers 5 or less moving forward.
well, no.

you'd need numbers 2 or less moving forward.
the new number decides what comes next.

in this case, it wouldn't matter which queue i join.
since i 2 is deciding factor of what comes next.

and in this case, it's just 532.

what about 53233

okay after 2 what can happen?

3 comes.
now, 3 can actually displace 2 and form a queue
with whatever 2 chose.

be it 52 or 32.

and why does this work, because, it's a monotonic stack.
pick a number and continue the non decreasing sequence.
if the new number is greater than the last.
pop the lasts until the new number can fit in.

what if one of the lasts were going to form a longer streak later.

say

522322

look at this, you'd have 522

then 3 bounces them, now you have 5322
problem is, this is length 4.

meanwhile, 52222 could have happened
and that's length 5.

what if it didn't replace.
it just found it's place.

rather than bounce the smaller numbers.
if you find a bigger number.

place it at the first number
it's bigger than or equal to.

well, what does that tell you?
why even do it?

the concern with 522322

is at 522, you want to make a decision.
what do i do with 3.

well, what can you do?
they obviously can't continue this streak.
but can take part of 5.

so, technically, i'd have two threads.

522
53

both explore, further.
53 fizzles out.

522 grows and continues.
and how would you model this?
different branches?

yeah.

every new number that doesn't continue, pops of numbers till it can fit.

and then it explores it's own branch.
you want to explore further first.
before popping, cause i think the back tracking is easier to write that way.

yeah, i'd have to try this some other day.
TODO start here 

they want to know the longest sequence with a non-increasing gap between elements.
it's the gap between elements that's non-decreasing.

not necessarily the elements itself.

542 is an invalid sequence because the gap between 5 and 4 is one.
while the gap between 4 and 2 is two.

hence the sequence of gaps increased from one gaps to two gaps.