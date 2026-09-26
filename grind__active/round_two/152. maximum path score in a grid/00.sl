i want to move from top left to bottom right
without exceeding the cost `k`

and how would this work?
i can move right, i can move down.
each cell has one of three values, 0, 1, and 2

each cell also has a cost.
the cell with value 0, has cost 0.
the cell with value 1, has cost 1.
the cell with value 2, has cost 2.

and how do i find the max score w/o exceeding `k`

well, at any point, i want to pick my next best cell.
how do you define that?

well,
i should always optimize for the cell with the bigger score.

the moment cost exceeds k, i drop that path.

so, start at top left.

it's giving max heap.
pick the cell with the largest score.

this isn't a heap problem.
you start of at a cell.

you explore right,
you explore down.

you pick whichever path is better.

so, first cell, what am i doing?
let's start with the smallest grid.

one cell, one column.

i go right, out of bounds.
i go down, out of bounds.

say i use `None` to signal out of bounds.

then i'd return what?
the score and cost.

of that cell.

okay, two columns, one row.

top left.

down returns None,
right returns what? itself.
the score and cost of said cell.

what does the parent cell do.

add it's score to the incoming score.
same as cost, then return.

that's the only path to the bottom.
i only need to check for exceeding `k`
at the end of the entire op.

if a cell has both right and down path.

the parent wants the best pick, either the right path
or the down path.

optimize for score first.
add to whichever is bigger.
if the cost permits, go ahead.

if not pick the other.

it feels like it's missing something, lemme implement and see.

// TODO rewrite this joint.