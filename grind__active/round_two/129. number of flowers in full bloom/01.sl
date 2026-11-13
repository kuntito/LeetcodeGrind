i have flowers, 
they bloom at a specific time.

for each flower, i know what time it blooms
and what time it stops blooming.

i have a guestlist.
people come in to see the flowers.
i know when they arrive.

what i want to know
is what flowers would be blooming when they do.

when the first person arrives, i ask.
how many flowers are blooming?
and i record the count.

it's simple enough to describe
so how do you write the code.

the arrival times should lead the decision.
sort the people by who arrives first.

no when that guy is around.
you want to hold the flowers that are blooming.

for the guy to see a bloom.
he'd need to come within the bloom window.

so, the ask is, how do you store a flower's bloom window.
what do i care about?

i care about the time the bloom ends.
if a person arrives on or before the bloom ends.
then they see the flower.

so, how would that go?
store based on bloom ends.
a min heap, so you always get the first bloom end.

you keep taking from the heap.
at each flower, you check if the person can see it.
if they can. record it.

you keep going till the -
hold up.

if you have a flower that blooms `3-10`
and you come in at `2`
would you see it?

well, no.
so, storing the ends is not enough?
well, it just means you don't consider that flower.

since, it's a min heap, you'd be storing (10, 3)

and if the time `10` is the earliest end time.
then that's what you check first.

just that, you check the start time too.
before recording.

but you could do all this, if the next person comes in at `3`
the flower wouldn't be there.

cause you removed it.
a heap might not be the best.

i need a structure that knows.
for each time period how many flowers are blooming.


one idea is to run through the ranges.

say, for 3-10, go through numbers 3, 4, 5, 6..
add an entry to a map.

so the map knows, at time `t`, this many flowers are blooming.
this would mean, go through the intervals for every flower.

doesn't sound like it'd be efficient.
let's see.

yeah, it's inefficient. hella large intervals break it.