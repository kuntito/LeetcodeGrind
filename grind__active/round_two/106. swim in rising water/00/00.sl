i have a grid of numbers.

i want to move from top left to bottom right.
however, this movement is conditional.

there's two conditions:

* how i can move, and
* when i can move

the how is, i can only move in four directions.
* up
* down
* left, and
* right

the when is based on time.
i start off at time zero.


i can only move to a cell when the time is right.

it's useful to think of the cell numbers as time.
you can only reach a cell when the current time is 

***
i have a grid of numbers.

i want to move from top left to bottom right.
but my movement is based on two conditions:

* how i can move
* how i should move

how i can move is what directions i can move to.
* up
* down
* left
* right

how i should move is what direction i should pick first.
i always want to pick the direction with the smallest number.

the question talks about time, how you can only reach a cell
when the current time is equal to the cell value or greater than it.

it makes it seem more complicated than it is.

if i have two cells, 
one has value `2`
another has value `1`

i'm always going to be able reach the cell with `1` 
before i can reach the one with `2`

and so, i can summarize the time logic as always pick
the cell with the smaller value.

once, i can do that.
the question becomes how much time would it take to get to the bottom right?

this would be the biggest cell i picked.

***
TODO:
address "the biggest cell you picked", if the biggest cell is top left, does it still apply?
address picking the smallest cell.
    yes, it's what you want, but you want to make it clear you're picking the smallest cell from a pool of cells you can reach.

