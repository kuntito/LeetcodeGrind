there's an abandoned rail network.
the mayor wants to revive it.

every station is connected.
some, in multiple ways.

to make a decision,
the mayor requests an inquiry.

which railroads can we absolutely not remove?
which railroads can we maybe remove?
which railroads can be completely removed?

so, how would i know if a railroad
can't be removed?

well, if it's the only one connecting two stations.
then we can absolutely not remove it.

and the ones, you can maybe remove.
well, it's one where -

this question is deceptive.
you're not dealing with a graph.
well, not really.

there's nodes, say the abandoned rail network.
you want to revive it.

but save costs.
the goal,
is to keep all the stations connected, and
keep the overall rail length to a minimum.

there's several ways to this.
and in all of those ways.

i want to know,
the roads that always occur.
and the roads sometimes occur.

and how would this go?
that, is the proverbial question.

how would it go?
well, pick a station.

what's the shortest station
it's connected to.

then from that station.
actually, no.

that's not how it works.
you pick a station,

you connect it to the closest station.
now, you're the guy at the starting point.
you now have two decisions.

where to go from the closest station.
and if to go somewhere else from the initial station.

how would you decide?

say, you start at `Kilimanjaro`.
you take three steps to `Forestry`

now, we're at a stand still.
from `Forestry`, i can go to `DeeperLife` in one step.

yes, but that's the wrong way to think about it.
you want take the shortest journey.

and so, from the jump
well, you'd pick any station
since, 
all stations would end up being connected.

what matters is what you do at each station.
i'm looking for the shortest journey.

okay, it makes sense to pick the shortest destination.
for Kilimanjaro go to Forestry.

now, what do you do.
well, you have two positions you can make a decision from.
where, is it cheapest to continue from.

so far, getting to Forestry, has taken 3 steps.
at Kilimanjaro, your only other destination is EmmanuelAdebayor.
and it costs 5 steps.

and what do i do with this information.
well, nothing yet.

i'm at Forestry
and i'm at Kilimanjaro.

from Forestry, i can continue on for one step, to reach
another station, DeeperLife.

which would mean my my original journey now becomes 4.

and from Kilimanjaro, my next stop is five steps away.
so, it makes sense to go to continue from Forestry.

if i get to DeeperLife, what happens.
now i have three places, i can decide from.

yeah, it gets crazy with every step.
that Dijkstra homie was on one
when he discovered this joint.

so, what the min heap does
or really, what you wanna do.
is hold the next best destination.

once you pick a station.
you line up the destinations.

pick the first one.
now, that first one, would, could
have it's own destinations.

just add it to the line.
and sort em.

but sort em on what?
well, the other guys
were lined up by their starting points.

and the new guys,
i jump, cause i know,
but they're lined up by ...

perhaps, redefine it.
at the start,

each station, had the cost
it would take to get to them.
from starting point.

i go to the cheapest one.
and from there, i can go elsewhere.
and now, the places i can go.

have the cost of what it took me to get here.
and what it takes to get from here to there.

and that's what i store in the destinations pool.
it's always sorted by the cost of getting to a station.

so, you'd always pick the shortest destination.
so, how then do several MSTs happen?

well, 
for one, starting from a different station
can give different results.

consider a triangle of stations.
  A
 / \
B - C

where each station costs the same from everywhere.
if i start at A.

my destinations are B for the cost of 1.
and C for the cost of 1.

if i go to B.
my destinations are now

C for the cost of 2.
and C for the cost of 1.

i go to C for the cost of 1.
so, the `B-C` joint is never used.

meanwhile, if i'd started from B.
i'd have visited A and visited C.
and the `A-C` joint is never used.

so, each node has creates it's own solution shape.

and is there a way where, 
there's multiple viable destinations.

yes, both things can be true.
at each step,
you can have multiple destinations that are true.
and that lead to a solution shape via different paths.

so, how do you know.
well, when you have competing destinations.
you try everyone, see what happens.

track the edges everytime you find,

so, what's the game plan.
explore every node as a starting position.

in each exploration.
you do this.

pick the cheapest next node to visit.
if there are multiple.
explore all.

once all nodes are seen.
save the set of edges in the graph.

when all said and done.
filter the homies that's always in, and the homies that's sometimes missing.
and you have your answer.

can we write this? why not?
