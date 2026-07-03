i'm given a grid and want to return an integer.

***

i have a 2x3 board.
it has six cells,
five of them contain the numbers 1 through 5
in a random order.

the sixth cell is empty

***

i have a board.
two rows, three columns.

the board cells contain the numbers
0 through 5, in a random order.

my aim is to order the cell values
so the board becomes..

1 2 3
4 5 0

i want to do this with the least amount of moves possible.
and return the number of moves made.

if the board is impossible to order.
i should return -1.

however, how can the board be impossible to order
all the values are there.

well, are there rules to the ordering?

i can only move the 0 around.
i can swap it with any number in the cardinal directions.

up, down, left and right.


so, really the question is,
what's the shortest path 0 can take
from it's starting position to bottom right.
such that the other cells are in their rightful place.

the first approach is, move 0 in every direction.
count each move.
once you hit bottom right, check if every number is in place.
record the result.

