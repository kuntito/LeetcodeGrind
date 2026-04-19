# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/

i'm given two things.

a 2d list of integers and a target.
target is an integer.

what do i want?

i want to find out the number of submatrices in 

***

i'm give two things.

a 2d list of integers and a number.

the 2d list is referred to as `matrix`
the number is referred to as `target`

the matrix is easier understood as a grid.
my job is to find out the number of sub grids, whose cells sum up to target.

and how would this work?

from each cell, where can i go?
for one, each cell is a sub grid.

and it can expand to form another sub grid.

if i start at origin, (0, 0)
i'd have my first sub grid and can determine if it's equal to target.

from this point.
i can go right one step OR go down one step.

whichever step, i get another cell.
my total cell sum is modified and if it's equal to target.
i should note it.

now, i'd be back where i started. i can go right

what i don't know is if i can go diagonally.
i'd attempt it without those directions and see where it takes me.

so from each cell, i can go right
or go down.

can i go up? if i went right, i can go up.
it seems i'd need to track visited cells so i don't go the wrong way.

so for each cell, i'd explore all four cardinal directions.
incrementing the total sum as i go along.
once, i hit a wall, i go back and pick a different direction.

at what point does it end?
well, it's when i'd have explored all the cells.

# TODO finish this..

a cell is a submatrix.

other sub matrixes can emerge from that cell.
they do so in three ways.

* incrementing x2, moving rightwards
* incrementing y2, moving downwards
* incrementing both, x2 and y2, forming rightwards and downwards, forming a larger square.