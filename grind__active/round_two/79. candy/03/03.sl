https://leetcode.com/problems/candy/description/

there are some children standing in a line.

i'm a candy man.
i want to give them candy.

however, there's rules to giving candy.
two rules.

one, 
    every child must receive at least one candy.
two,
    if a child has a higher rating than it's neighbors, 
    the child must receive more candy than it's neighbors.

    but what's a rating?
    a number associated with each child.
    every child has a rating.

    every child has neighbors.
    a left neighbor and a right neighbor.

    a child at the left edge has no left neighbor.
    a child at the right edge has no right neighbor.

    the idea here is the child must have more candy
    than it's highest rated neighbor.

    in essence, both neighbor's candy should be determined before
    the child's candy.

there's an order to which i'd give candy.
the least rated child should always go first.

so, sort the list by ratings?
iterate through the ratings.

i'd have to know the position of each rating.
it makes sense to pair them with their indices.

the idea is this, for each rating.
i'd set it's candy count to `1 + highest rated neighbor's candy`

and if there's none?
i'd simply assign it `1`.

iterating through ratings ensures the lower ratings get assigned first.
on each rating, i'd grab the index.

check the left and right neighbors.
if they have lower ratings, they'd have candy.

with this, i can determine the candy for the current rating.
and if they have no neighbors or higher rated neighbors.
i'd simply assign `1`

okay, so how are you sorting the candy by ratings?
a minHeap

iterate through the ratings.
append the heap item, (rating, index)

then i need somewhere to store the candy for each index.
a hashmap maybe?

or an index of the same size as ratings?
`candyGiven`
