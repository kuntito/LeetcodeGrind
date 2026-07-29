obstacle

yet another diagram.

am i sentenced to a life of obstacles?

what's wrong with questions with just strings.
why'd there have to be an obstacle.

...

i have a grid, and want to return an integer.
i have a grid, and want to return a number.

shorter, and better.

i want to move from the top left of the grid
to the bottom right,
following the path with the least obstacles.

well, really, 
they just want to know the number of obstacles on said path.

so, how'd this go?
at cell one, i can turn left, right, down, up.
i'm like a dancing Rasta.

anywhere, i go.
but how do i know the path with the least obstacles?
i think it's that Dijkstra joint again.

you consider every where you can go at once.
you pick the one with the least obstacles.

add more destinations.
re-consider.

pick the one with the least obstacles.
at some point.

you'd pick the bottom right cell.
at which point, what do you do?

that has to be your answer.

since, 
i picked the cell with the least obstacles to go to?

i'm spiralling again.

at each point, you're making a decision.
which cell do i pick?

you always want the cell with the least obstacles so far.
and so, by the time you hit bottom right.

you'd have the cell, the path with the least obstacles.

each cell in this terrain is really a node along the path.
the node knows it's coordinates, and how many obstacles it'd seen so far.

you also don't want to explore the same position twice.
since, the first time, you see it,
is the least obstacle path to that node.

can i solve? i can attempt.