two arguments, an array and a 2d array.
the output, an array.
***

two arguments,
an array of integers, `queries`
and a grid of integers, `grid`

for each number in `queries`
i want to find out how many grid cells
i can reach following a condition.

well, two conditions if i get into it.
to find the grid cells,
i must start the exploration from the top left cell.
i can only travel in cardinal directions
and can only travel to cells if the cell value is kess tgab

***

two arguments,
an array of integers, `queries`
and a grid of integers, `grid`

i want to return an array
representing the result of each query.

`queries` contains numbers.
and for each one,
i want to find out the number of grid cells
lower than the current query.

however, there's two conditions to finding these cells.
one, 
    i must start checking from the top left cell.
two,
    i can only travel in cardinal directions.
    
the iteration path stops when i hit a cell value
greater than or equal to the current query.

HOW TO SOLVE

what's the approach?
well,
for each query,
start a recursive search
track visited cells that meet requirement.
increment, count.
save in return array.

TODO write the code.