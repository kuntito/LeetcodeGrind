there's terror in my eyes,
as i consider tackling this question yet again.

i say i know what i must do
and ran out of time before i could do it
so this time,
i just have to do it.

well, yes.
what's step one?

um, i'll think about it in terms of what i want to do.
i have a graph.

i want to find the different MSTs
it can have.

while tracking two things.

the edges that appear in every MST,
and the other edges.

so, step one,
is gathering every MST.
to be fair, i only need all the edges in the MST.

fair.
so, i'm gathering,
sets of MST edges.
i can probably track the solution as i go along.

if i load all edges in a hashmap.
and increment MST presence.

at the end, i'd find out all pseudos
i'd keep a dummy edge, say `-1`
and this i'd increment on every MST.
it tells me the total MSTs explored.

i'm doing it because it's not clear
to me, if saying the edges with the most increments
are all critical.

so, can you write the code.
yes.

***
well, no.
in order to explore every MST, 
i have to consider situations
where there's several same costs paths to take.
tried to strongarm it and write without that.
but it simply won't work.

take a square graph.
where node c connects to d
and node a connects to d.

by the time, node a, b, c are connected.
there's two ways to connect d.

via c.
or via a.

both are MSTs and both are valid.

in essence, to implement my idea
i need to write an algo that can see
the next two destinations have the same cost.
let's see what happens when i go down this road.
and what happens when i go down the other one.

collate your results at the end.
each path can start several paths too.
it's recursive till the end.
the plot thickens.

till tomorrow.