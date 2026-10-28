i would attempt this question.

but it's seems tough.

i can't picture what progress looks like.

what's the max number you can find?

well, the starting point for a binary string
is how many of the early parts of the string can you change?

can you make higher?
and how would this go?
a 1 is worth more than a zero.

so, if you start with 00, you can always change to 10

i mean, look at it this way.
the first two strings are one of:

00
01
10
11

for 00, you can flip for a higher number.
for 01, you can't do anything, so you leave as is.

for 10, you can flip to 01, but that would be a smaller number.
so leave as is.

and for 11, you can't do anything, so you leave as is.

it's a question of exploring every two characters
and increasing if possible?

running through the examples.
it seems i run through a window of 2 through the entire string.
increase everything that can increase.

then go through the window in reverse.

it's not an algorithm, i came up with.
i just wrote BS.

there's two types of things you can change.
you want to know if to change it.

to be fair.
you should always change.
well, it's true for an increase.

you should always increase.
you shouldn't always decrease.

the move is 00 -> 10, that's an increase.
the second move is 10 -> 01.

so, the question is:

when is a decrease wrong?
or rather, when is it right?

intuitively, i'd say when it's in the second half of the string.
is that always true?

i don't think i'm even thinking about this right way.

00 -> 10, doesn't mean increase.
it actually does.

and 10 -> 01 is a decrease.

okay, so always increase.
that's a good point.

always decrease, well no.
you only want to decrease if the decrease brings an overall increase.
so back to the question, how can you tell?

110 is bigger than 101

i think i just got it.
the aim is to have as many `00`s as possible.
a decrease is only a means to that.
and the intention behind it,
is 10 -> 01 shifts a 0 leftwards.
so, it's a good move to spam it so it hits a zero behind it.

and if there's no zero behind it?
then no need to spam.

what if there's zero and it can't reach it?
how so?

it'd have to start with `10` first.
then behind it, is either a 1 or a 0.

if it's a zero, we're in luck.
since, i'd have a `00`
and if it's a `1` then it becomes a `10`
in essence, as long as there is a zero behind a `10`
you can spam the second move till the zero hits the previous `0`
and when you hit, do you stop?
well, you carry on the window move from that point onwards.

it's still a 2 element window.
you move in search of `00`s incrementing as you go.
and tracking the number of zeros you've left in the dust.

so, if you every hit a `10`, you know you can create a `00` behind.

it works but TLE.
how can i make this faster?
