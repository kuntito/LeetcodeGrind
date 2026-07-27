they drew a diagram.

a diagram. 😒

when they draw a diagram, you know it's over.

they got squares and everything.

i remember `trapping rain water i`
i nearly lost my mind.

yet, they made part 2.

okay, from the looks of it, i have a 2d array.
and want to return a number.

that's not so bad.

'pparently, each square of the grid represents elevation.
and they want to know, 
how much water the grid can store
if it rains.

so, really,
i just need to know how much water
i can store in each square
and sum up all the squares.
the things i stored inside them i mean.
the water.

this is the simplest question in the world.
they should fire the guy who said it's hard.

for each square, i can tell how much water it can store.
by the squares around it.

well, the shortest square around it
decides how much water it can store.

cause there needs to be a gap between
the square and it's shortest surrounder.

that gap is how much water, it can store.

let's write the code.

i failed miserably.

it's not necesarily the smallest surrounding square.
it's the smallest surrounding boundary.

at each square, you're saying:

as far as the eye can see
is there a taller square than i, to the north.
to the south, west and east.

and the smallest of those,
is what determines how much water i can store.

and the seeing is where caching comes in.
i see why it's labelled hard.

apologies, mr LeetCode.
i spoke too soon.
you should be reinstated with a slight bump in pay.