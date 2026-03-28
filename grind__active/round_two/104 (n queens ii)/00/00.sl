the question is, how many different ways can i place `n` queens on an `nxn` chess board such that no two queens are attacking each other?

following the rules of chess, a queen can move in the ordinal directions.

up
up right
right
right down
down
down left
left
left up

to place eac queen on an n by n board where they are not attacking each other would mean each queen is on it's own row.

but where on the row?
it's hard to say without seeing the board.

it's best to take it one at a time.

place the first queen at row one, column one.

then the next question, where to place the second queen on row2.

she can't stay on column one, because, the first queen can attack her there.

she can't stay ib column two, cause the first queen can also attack here there, a diagonal attack.

she'd have to stay on column three.

okay.. i seemed to have jumped the gun here.
i don't even know the board dimensions.

i'm already placing queens.
that's a fair point.

what i would say is, it's clear a board of size `1` and size `2` would not work.

since at minimum, the second queen needs to be at column three on row two.

...

i'd say the idea here is 
for each row, place a queen.

you don't know what column so you have to check it all.

once a queen has been placed, you'd need some way to know the cells they can attack.

the queen can attack in eight directions.
so i need to store all eight? well, not really.

if a queen is on column two, i can store in a set, that column two is no longer available.

this accounts for up and down.
same for rows, i can store the row in a set, and make it known that the row is unavailable.

and the diagonals?

a trick i learned from the early days,
the diagonals can be identified by adding or subtracting their indices.

the forward slanting diagonals.

00 01 02
10 11 12
20 21 22

i.e. `02 11 20`
their indices all sum up to `2`
as row index increases, column index reduces.
it's a pattern.

so if i store `2` in a set for forward slanting diagonals, i can also know that diagonal cannot be accessed.

the backward slanting diagonals are somewhat similar.
for this, as the row index increases
the column index increases.

ergo, their difference would always be the same.

`00 11 22`
for these, the difference would be `0`
ergo, i can store this value in a set for backward diagonals.

so four sets.
verticals
horizontals
forward diagonals
backward diagonals

iterate through each column for each row.
if you find a valid position, place the queen.

move on to the next row.

you keep doing this until two things.
you run out of rows.
you run out of columns.

if you run out of rows.
it would mean, you've placed every queen somewhere.
you can update the global count for distinct solutions.

if you run out of columns,
you go back the exploration path.

what does that mean?
it means the way you've placed queens, there was no valid way to place another queen on a different row.

and so you go back.
when you do go back, you unplace the queen and put her in a different position.

my writing today isn't the best.
perhaps, i'd just solve it and get a move on.