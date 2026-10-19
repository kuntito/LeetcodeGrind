i'm given two arrays, and want to use them to make a grid.

the arrays are named, `rowSum` and `colSum`

and the grid, i'm making should have the same number of rows
as elements in rowSum.

same as colSum.

in essence, i know the grid dimensions.

now, i just want to fill it with data so the rowSum and colSum
mean what they say.

the idea is, every integer in `rowSum` is the sum of the the elements
on that row.

same goes for columns.

so, how would you go about this.

well, create the grid with zeros.
then run through each cell.

or no, the cells can remain zeros.
why not just place the row sum values
at the start of every row.

leave other cells in the row blank.
the for col sum,
place the col sum on the first cell of every column.
leave everything else as 0.

the only concern would be the first row, first column.
what goes there?

what really is the problem?

i think it's the core of the problem.

the first column needs it to be a certain value.
the first row needs it to be another value.

i mean, by my logic, i can't just place both there.
say i place the column.

then the row needs somewhere to go.
it can pick any of the other cells on the row.
the problem is, every cell where it's added

it increase the colSum of that column.
negating the entire problem.

in other words, this plan wouldn't work.

yeah, imma look for answers.

TODO start here. i don't know how to solve this.
# https://www.youtube.com/watch?v=Ks6fGnXkHPg
2:16