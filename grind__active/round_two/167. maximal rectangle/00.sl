i have a grid, 0s and 1s, is all it has.

i want to find the largest rectangle containing only 1s.

well, a rectangle is repeating streak of 1s
across a vertical axis

or a horizontal axis.

so, for every streak of 1s.
which ones occur the most and span the most.

it'd probably be TLE but it could work.

and how would you explore?
a streak can start at any cell.

so explore every cell?
well, no.

if you have a 1.

you could be dealing with the start of a horizontal
or vertical streak.

explore both.
the vertical aims to keep going down.
till it stops.

then it moves right, till it stops.
when it does, calc the area.

the right move, is saying, can i get this many ones
on the next col, if not, stop. if yes, continue till stop.

and the horizontal aims to keep going right till it stops.
when it does, it asks, for this streak of 1s
does it replicate downwards?

if not, stop, if yes, continue til' stop.
can i write it?

let me see.
