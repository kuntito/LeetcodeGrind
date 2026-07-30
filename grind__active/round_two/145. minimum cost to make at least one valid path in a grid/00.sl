i have a grid.

it's cells contain one of four numbers.

1, 2, 3 or 4.

the numbers represent direction.

1 means right.
2 means left.
3 means down.
4 means up.

i start, top left of the grid.
i want to reach, bottom right.

following the directions.

the grid, as is, 
might not have a valid path from top left
to bottom right.

and so,
i'm allowed to change the direction of any cell.
but for any cell,
i can only change direction once.

i have as many cells as changes.
and each change can only belong to one cell.

if a cell's direction has been changed,
it can't be changed again.

i want to construct a path from top left
to bottom right, 
without spending more changes than i need to.

how would this go?

Dijkstra.

at any point,
i want to pick the cheapest cell to visit.

i keep doing this, till i hit bottom right.

by then,
i'd have taken the path with the lowest changes.


***
what am i optimizing for?
least effort cell?
how do you define least effort?
a cell with the same direction as you.
and if there isn't?
pick any cell.
        
actually i'm optimizing for my own direction.
at top left, i'm facing somewhere.
it could be another cell, it could be a border.
        
the question at each point is:
one, where's the cell in my direction?
if there isn't one, 
then i need to change my direction.
but to where?
to any cell.
        
consider:

<- ->
<- ->

at top left, i'm facing left.
not facing any cell, so i have to turn.

my options are right or down.
seeing it, i know to pick right, not down.
but why?

actually, right can't go anywhere too.
this is the example, i wish i had:

<- -> ->
<- -> ->

i know to pick right here, not down.
but your algo would have to address the case.
where both cells can go nowhere.

each cell should know if it can go somewhere.
perhaps, it's a question, i can ask?

you want to pick a cell that can go somewhere
and if there isn't one.

you pick any cell.

for this guy:

<- ->
<- ->

i know top left has to change.
then i have to pick one cell to go to.

none of my options can go anywhere,
so any one would do.

and for this,

<- -> ->
<- -> ->

i know i have to change top left.
to where, the cell that can go somewhere.
in this case, the right cell.

so that's what i'm optimizing for.
pick the next cell that can go somewhere
or pick any cell.

and you can further sumamrize 
as sort cells by which can go somewhere.

and by extension,
the front of the queue is always what you want.

`TODO, i'm circling round the answer.
need more time.`