i'm turning a grid to a int.

the numbers on the grid are, at least, `0`.

and each number reps the time it's position is available.

***

i'm turning a grid to an int.

i'm standing top left of the grid
intend to reach bottom right.

i can move left, move right, up or down.

each grid cell, contains a number,
a number represents the time the cell is available.

not sure available is the best word for this.
i'm walking on the grid, walking in one of four directions.
but not every square of the grid, is available.

say, there's certain cells that blow up if stepped on befor-

***

i'm on a grid.
top left.

want to reach bottom right.
i can walk on each square.
but only when it's available.

define available?
when the cell's time has been reached.

what do you mean?
each cell has a number.
the number, says at what o' clock,
the cell becomes available.

okay, i start at time zero.
to move at any point,
i only have four directions
up, down, left or right.

what's the smallest time it can take to reach bottom right?
if every move takes 1 second.

HOW TO SOLVE...

well, at each point,
you move to the next available cell.

define next available,
the one who's time has been reached.

so, sort destinations by their time, lowest to highest.
then pick the lowest one always.

by the time, you reach bottom right.
you'd have taken the shortest path, time wise.


