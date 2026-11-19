let's have another crack at this.

i'm going through the line, 

at each person, i want to ask
is there any one after them that meets the condition.

and i'm asking if i can precalculate the condition.
what would this look like?

what does each person need to answer.
of the people after me, shorter than me.
who's the tallest.

yeah, it's not so simple then,
well it is, if you iterate backwards.
and hold the tallest person you've seen.

yes, that wouldn't answer the question.

consider:

    2, 4, 1

2 the tallest shorter person after 2 is `1`
and so tracking the tallest doesn't help.

but can 4 help.
how so,

if you know the tallest person.
they just need to know the shortest person after them.

so, what, shortest array.
and tallest array.
calculated from behind?

how would this work.

for each index, i know the tallest person after this point.
and after this point, i know the shortest person.
so can answer just by iterating through the array once.

i just need to pregen both arrays.