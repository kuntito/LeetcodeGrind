https://leetcode.com/problems/reconstruct-itinerary/

i'm given a list of plane tickets, and asked to connect them, so they form a valid route.

what do you mean connect?
it means match the destination of one ticket to the departure of another ticket.

say you have two tickets:

LDN to AMS
AMS to EGY

you can connect them at AMS.

okay, so i want to do this for all the tickets.
yes, but your starting destination must be JFK.

so, how do i know where to go next after JFK?
well, you'd have to go to find out.

so, check all destinations.
and what does a valid route look like?

you'd have to have connected all the tickets.

there is one condition, it states if there are two valid paths
take the one with the smallest lexical order.

what does this mean?
if you have two destinations, and it doesn't matter which comes first.
pick the one that's alphabetically smaller.

what does alphabetically smaller mean?
it means the one that'd come first in the dictionary.

so ABC over ABD

fair.

i can make this decision at each airport.
just explore them in dictionary order and if i find a valid path
i'm guaranteed it's the alphabetically smaller one.

the bigger question is how do i know the valid path?
well, from JFK, pick the alphabetically closest airport.

when you get there, do the same again.
that's recursion.

yes.
keep doing it till you can do it anymore.

at which point, you'd be at an airport where there's no destination to go to.
now, this could be because, you've visited everywhere.
or you took the wrong path.

what's the difference?
if you've visited everywhere, you'd have no tickets left.
if you haven't, you'd still have unused tickets, just that they're from different airports.

`so, i'd need a way to track tickets left on my travels`

in the case where i have visited everywhere, what do i do?
that's the end.

you'd store the itinerary.
well, i guess.

the aim of this is to return an array of the visited airports in order.
so you'd have to be tracking airports as you visit them.

so at the end. your array would contain the result.
so, can i simply return this?

well, you'd have to address the second end case.
the one where you can't go anywhere from the current airport
but there's unused tickets.

i think i can return two things.
the tracking array, containing the airports visited so far, and a boolean indicating whether i've exhausted all tickets.

if i've exhausted all tickets, i know to simply return the array up the recursive stack.

if not, i know to pop the last visited airport and try another one.

seems like a solved problem.
how do i know if i've exhausted all tickets?

we can determine the number of checkpoints from the jump.
if you have two tickets, you'd have three check points.

LDN to AMS, AMS to EGY

AMS is a single check point here.

the same principle for three tickets.

every ticket except the first one represents one check point.
so, `if the length of the tracking array equals the length of tickets plus one,
then i've explored all tickets`

and what does the code look like?

before then, how do you handle used tickets.
the first idea i had was to iterate through every airports destination in order
this naturally handles the used tickets
since iteration is one-way

but what happens when you revisit an airport.
would you restart the iteration?

way i see it, for each airport, i can store the destination in reverse
and then reverse iterate through it.

popping every station and storing it in a different array.
you could but it's not a good representation of state.

at each airport, you want to see available destinations.
once, you visit a destination, it gets taken out.
