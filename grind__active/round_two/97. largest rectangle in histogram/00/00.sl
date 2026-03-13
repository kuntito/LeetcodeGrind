i'm given an array of integers.

and i want to find the area of the largest rectangle?

i think the rectangle bit makes it harder to reason about.

say, the array is:

[2,1,5,6,2,3]

each number occupies a slot.
`2` occupies idx=0
`1` occupies idx=1

each number is said to have a reach.
the number of consecutive slots a number can occupy.

a number can only occupy a different slot, if the number at that slot is
greater than or equal to the number.

not the best explanation.
***

i'm given an array of integers.

each integer is assumed to be the height of building.
so the array would represent buildings next to each other.

each building has a rectangle.

what's that?

a rectangle is...

how many buildings to the right are at least my height
how many buildings to the left are at least my height..

and the count of all these buildings represents the height of the building..

not the best explanation.
***

i'm given an array of integers.

each integer can form a clique with it's neighbors.
the clique can only be formed between consecutive neighbors
and the requirement is for every neighbour, to join the clique,
your height cannot be less than the main.

***

i'm given an integer.

each integer, wants to form a clique.
a clique is formed between an integer's consecutive right neighbors
and it's consecutive left neighbors.

but, there's a caveat. for a neighbour to join the clique.
the neighbours value cannot be less than the integer's value.

the neighbours value must be greater than or equal to the integers value.
every left, and every right, neighbor that fulfils this criterion joins the clique.

the streak extends until someone breaks it.
at which point, we determine the clique value.

the value of a clique is the number of homies in the clique times the value of the main integer.

consider:

[7, 5, 8]

`7` wants to form a clique.
it needs neighbors that are >= `7`
on it's left, there's none.

on it's right, there's `5`, but five is too low.
and so `7` is in a clique of his own.

his clique value is `7`

then there's `5`
she wants to form a clique.
on her left, he has `7`.. a worthy member
so `7` joins the clique.

there's no other neighbor left of `7` so we explore rightwards from `5`
on her right, she has `8`, a worthy member.
so she adds `8` to the clique.

there's no further neighbors right of `8`,

so the clique is effectively:

`7, 5, 8`

and the clique value?
number of participants x value of main integer, `5`
so, we'd have `3 x 5`
`15`

then we move on to `8`
eight has no worthy neighbors to the left and none to the right
so `8` rolls solo, a clique of one.

after seeing all the cliques of every element.
i should return the highest clique value.

in this case `15`