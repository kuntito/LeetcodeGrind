i have a chess board.

i want to find out the number of ways
i can place a queen on each row
such that no two queens attack each other.

***
so how'd this work?

you place a queen on one row.
place a queen on another row.
when you run out of queens.
and rows.

you have one way.
what if you run out of rows before queens?
can't happen.

you have enough queens for each row.
what if you run out of queens before-

well, this an insight.
you can't run out of queens or rows.

what you can run out of,
is viable board positions.

once that happens before placing every queen.
you circle back and try a new position.

perhaps, this needs more resolution.

the first queen you place, is on a row.
a row is made up of columns.

so queen first, goes first row, first column.
queen second, goes second row, but which column.
not the first, since she'd be under attack from queen first.

so, she can go second row, second column.
queen three, third row, third column.

queen four, fourth row...
actually, i haven't paid attention to other queens attack ranges
outside the vertical.

it's not that you place queens on each row.
it's that for every row.

there's viable columns.
you place a queen in all of them
see what happens.

you place the first one.
okay, what does this mean for the other rows.

that's what we figure out.
once you place a queen,
it's column is no longer viable for any other queen.
neither is that row.
neither is it's diagonals.

so, for every queen placed.
you track this.
this way, when you get to the second row.
you know what columns are viable.
you place a queen in all of them.

and repeat.
it'd probably happen at some point.
you reach a row and no viable positions.

what do you do?
well, you go back to the previous row.
try another viable position on that row.

this is that backtracking joint.
it's a trial and error method.

several viable options.
for each one, place a queen
see if you can place the others.

if you can increment count.

HOW DO YOU TRACK VIABLE COLUMNS.

for one, i've used columns in writing,
but cell, communicates the intent better.

a cell is a position on the board.
this row, this column.

so, the question should be,
how do you identify viable cells.

okay, for the first queen.
all cells are viable.

all cells on the first row.

she iterates through all of them.
sees how things pan out for the other queens.

now, the moment she picks a cell.
that row is no longer viable.
her column is no longer viable.
her diagonals are no longer viable.

rows are represented by one number. rowIdx.
columns represented by one number. colIdx.
diagonals are represented by two numbers. rowIdx and colIdx.
there are two diagonals.

is there a relationship between the numbers 
that lets us identify a diagonal?

00 01 02
10 11 12
20 21 22

looking at the diagonals.
the longest ones.

`00 -> 11 -> 22`

and

`02 -> 11 -> 20`

one leans left, `00 -> 11 -> 22`
this leans right, `02 -> 11 -> 20`

what's the pattern here?

rowIdx and colIdx in the left leaning diagonal increases.

the right leaning,
    rowIdx increases
    colIdx increases

TODO
    seems like i'm working my way to dismantling this question.
    since, i've observed a pattern
    how does this help me identify a diagonal?

    for the right leaning, where row idx increases
    and col index decreases.

    the sum would always stay the same.

    let me not get into this now.
    till next time.