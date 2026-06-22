i want to return a list of integers
after receiving two inputs.

there are buildings
ordered left to right.

two people, Alice and Bob,
want to meet.

i'm told their current buildings.
however, each person has a rule for moving buildings.

if they move,
they only move rightwards
and only to a taller building.

Alice can meet Bob, if Bob's building is taller.
else, they'd both need to move rightwards
till they find a building that's taller than 
where any of them had been.

i'm given a list of starting positions
for Alice and Bob.

for each starting position,
i want to find the index of the building where they meet.

and if no such building exists, i'd note that with `-1`.

the collection of indices or -1s is the array i return.

***

now, to solve.

take a pair.
what's the question?

can Alice meet Bob, where he's at?
if yes, meet.

if no, find the nearest meeting point.

repeat till query exhaustion.

TODO, rewrite, i assumed Bob is always right of Alice.
that's not always the case.