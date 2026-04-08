i'm given a list of numbers, `nums`

i want to remove all the numbers from the list.

one after the other.

but i simply can't remove any number i want.

with any number, i remove, i gain coins.
with each number, the coins vary.

i always want to remove the number that gives me the most coins.

and how do we know how many coins removing a number gets us?

the number of coins is this:

a product of the number you're removing, with it's left and right neighbors.
if there are no neighbors, use `1` as a placeholder.

okay.. but how does this help me determine the first pick?

for the first pick, i can run through the list and determine the coins for each number.

then remove that number.

and the next pick?

do the same?..
well, i could but it'd be inefficient.

each number wants to know it's left neighbor and it's right neighbor.
once you remove the number, you create a gap.

the left and right neighbors join to fill in that gap, and they become their new neighbors.

the problem now is,
what's the best pick?

i don't see a way knowing the first iteration's results helps me with the second one.

does it not?

well, after the first iteration, i'd know the coins i can get for removing each number.

when i remove the number, it's left and right neighbors are affected. i'd need to recalculate their coins.

every other number stays the same.
that way, the first iteration serves as a cache for all the numbers
except for two numbers, the neighbors of the number you remove.

okay, so how can i always have access to the number i want to remove?
well, two things.

* you always want to know the number that allows you remove the most coins.
* you want to remove that number and adjust the coins of it's neighbors.

i can use a maxHeap for the coins, 
the heap item would at least contain `coinValue`

say i remove the number, what then, how do i grab it's neighbors and update their values?

you could reference each number by it's index.
you could keep a reference for each number and it's neighbors.

numberIndex => [leftNeighborIndex, rightNeighborIndex]

every number should have this.
when you remove a number, you simply have to grab the reference for both it's neighbors and update them.

well, yeah, but how then do i update the maxHeap for the new coin values.
and to remove the old ones.

i think the reference entry should be..

numberIndex => [leftNeighborIndex, rightNeighborIndex, coinValue]

now, whenever i remove a number
and update the coin values for it's neighbors.

i'd also update the max heap, and the heap item would contain two things.
(coinValue, numberIndex)


TODO
the top item in the heap should point to the next number i want to remove.

unless, it's a stale value.
a stale value would be one where the coinValue was based on a previous version of the array.

in which case, the item i want is the the first item on top of the heap whose coin value matches what's in the array index reference.

