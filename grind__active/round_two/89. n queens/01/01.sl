i'm told how many rows a chess board has.

and asked to return the different ways
i can place a queen on each row,
such that no queen attacks each other.

***
i want to place a queen on every row
of a chess board, such that no two queens
attack each other.

***
i have a chess board.

i want to place a queen on every row.
i want to do this in a way that no queen
is under attack.

***
i have a chess board.

i want to place queens on the board.

one queen per row.

***
i have a chess board.

i want to place queens on it.

one queen per row.

when placed,
no queen should be attacking another.

i want to find out every way
this is possible.

for each way, 
i'd represent the board with strings.
each string representing a row.
each character representing a column.
the empty columns are represented with `.`
the queen is represented with `Q`

HOW TO SOLVE
    well, place one queen
    first row, first column
    then place the next queen.

    repeat till exhaustion.