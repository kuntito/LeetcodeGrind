# https://leetcode.com/problems/largest-rectangle-in-histogram/

step one, read the question.

given an array of integers, `heights`. i have an array of integers and it's called `heights`.

the array represents the histogram's bar height. what histogram? the one in the image.
it makes it seem like we've spoken about a histogram elsewhere.

perhaps, poor wording.
the array, `heights`, represents a histogram, where the width of each bar is `1`. i'm assuming the values in `heights` refer to the height of each histogram bar.

it wasn't explictly stated, but the naming of the array plus the diagram reveal it to be so.

my job is to find the area of the largest rectangle in the histogram.

each bar on it's own is a rectangle.
well, yes.

but what would the largest rectangle be? the largest bar?
not necessarily so.

the image shows how a rectangle can span mutliple positions.
it's not a rectangle per se. each bar is a rectangle, but the question is, can you draw a rectangle across several bars such that it increases the area of the rectangle.

not the best explanation.

a read of my previous attempts paints a clearer picture.

think of each bar in the histogram as a person.
the number, the height, can be treated as the person's clout.

now each person wants to form a clique with their right neighbors.
as many consecutive right neighbors meet their criterion.

and what is that criterion?
it's whether each consecutive right neighbor has the same or more clout as the previous neighbor.

if they do, they can join the clique.

now, the largest histogram, really, is the number, the person with the largest clique.

the clique size is the clout of the first person multiplied by the number of people in the clique.

this is what's going on when we draw a rectangle across the histogram.
if you have a [2, 3]

from 2, you extend a line from it's top rightwards.
the line can keep going as long as the right neigbor is at the same height or higher.

the line must keep grazing/touching next neighbors and that's what determines the size.

for a brute force attempt, i can check for every number, how many people in the clique.

let me try that then see how i can optimize.

`fundamental error.`

a clique can be formed rightwards and leftwards.
i assumed only right because the examples i saw, worked as so.

but consider: [2, 1, 2]

height `1`, can form the largest clique, since it has two guys, one on either side.

and so the algo, should spread in both directions.