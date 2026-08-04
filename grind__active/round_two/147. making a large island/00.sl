turn a grid to a number.

how so?

the grid cells contain 0s or 1s.

i want to find the largest connecting group of 1s

define connecting?

a chain of 1s where their cells are connected
in any of four directions: up, down, left and right.

and.. i'm allowed to change a 0 to 1
to get a larger group.

but only one `0`.

and how would this go?

nut case, change every zero
see what the 1s is,
track the largest one.

that's a start, let's see what the fuss is.[[1,0],[0,1]]

TLE.. need to optimize.