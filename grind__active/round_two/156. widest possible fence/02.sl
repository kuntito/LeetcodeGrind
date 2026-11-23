this question is nuts.

i must salute to the kings.

but first, what are we doing here?

they say planks of height, and say, widest fence.
which is it? a wide fence or a tall thing?

nonetheless, you have a list of numbers.
or say, a ..a list of gold bars.

actually, the planks make sense.
even if they're vertical bars.

i see.

you want a fence.
a fence made of vertical bars.
you want the fence as wide as possible.
but all the bars the same height.

so, two constraints.
how would you go about this?
i'd say, start with the bars that occur the most.

and see if you can get more those using the others.
or really, get as many more as you can by combining the others.

save the results.

then the bars that occur most the next.
and repeat.

eventually, you'd try everything and have an answer.
can you write it?

yo, how am i checking how many of each plank i can form?
for one, take the whole ones first.

then with the rest, how many ways distinct ways
can i form this.

yeah, here's the next bit.
given a list of numbers.

and a target.
how many ways can combine the numbers to form target
assuming i can use a number once.

and how would this go?
pick a number.

say, the smallest one.
if it's bigger than the target.
there's no way to form a target.
the smallest number is too big.

now, if it's less, what do you want?
well, get the next smaller number.

together do they sum to target,
if yes.

take those numbers out of consideration.
restart the operation.

address `1, 1, 2`
where the target is 3.

you pick 1, pick another 1, pick 2.
now, you have 4.
and it won't work.

so you drop2, drop1, and you're back where you started.
i guess the unspoken choice, is

at the beginning, you pick the smallest number.
now, your next number could be any number.

in which case, there's still no reason to sort it.
any number could go.

just explore every unique combination.
i see, is this a combination
no, you're trying to define it

don't define it.

what do you want to do.
pick a number.

then you have a list of candidates.
explore all to see what happens.

well, sorting helps you know not to go any further.
i agree.

so, pick a number.

who's the next pick.

pick them, see what happens on that journey.
whatever happens pick another candidate.

you'd be exploring every path.
and when does it end, when you exceed or reach target or run out of numbers.

so, what are you doing on each iteration.
or how do you start the iteration.

well, the same concept,
you have candidates.

and you'd have to start from one.
you pick one.
now, you have a new list of candidates.
so, you want to maintain a list of candidates.

that's what the array is.
and so, you pick the number.

start another call.
new start idx, cur ..

i need to restrategize.

for one, i can combine at most two numbers.
didn't solve.