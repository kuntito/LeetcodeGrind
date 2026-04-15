# https://leetcode.com/problems/first-missing-positive/

i have a list of integers.

i want to find the smallest positive integer that is not in the list.

smallest positive integer? what does that mean?

positive integer means the number i want is greater than zero.

to know the smallest positive integer not in the list.
i need to know all the positive integers in the list.

do i?

smallest indicates i just need to know one number.

if the integers were sorted, i'd check for every number after zero?

i'm going on a tangent here and i didn't fully state the question.

***

i'm given a list of integers.

i want to find the smallest positive integer not in the list.

in simpler terms, i want to find the first positive integer not in the list.
what does first mean?

if you consider all the positive integers in order:
1, 2, 3...
the first one in that series that's not in the list is what i'm looking for.

the question also demands i do this in O(n) time and in O(1) space.

i can start, saying `1` is the smallest positive integer in the list.
what if i explore the list and find `1`.


in that case, i have to assume `2` is the result.
what if `2` is in the list, then `3`?

you can keep increasing the numbers but the list is unsorted.
if you assume `1` is the result and you find `1` at the end of the list.

you can't just assume `2` is now the result.
since, you never bothered to check if `2` is in the list.

unless you store all positive integers somewhere.
i can't store it somewhere cause i'd be doing more than O(1) space.

but with the way the question is, some form of storage is necessary.
i need to know what positive items i've seen to know the ones i've not seen.

perhaps, this is the clue.

if i can't store elsewhere, can i store the result in the array itself?
how so?

what am i storing?
every positive integer i've seen?

and how would that go?
how would i know what's where?

that's where indices come in.
what do you mean, the index tells you where the number should be?

it's still unclear.

if i find the number `2` in the list.
what do i want to do?

you want to store it in a way that it's accessible.
you want to know where it is.

how would you do this?
store it in index 2? well, i guess.

that does help you know where it is.
but what happens to the content of index 2

for one, if it's negative or zero, you can simply override it.
if it's a positive integer, say `8`
you can do the same and place it at index `8`

and what if there's no index `8`
it doesn't get placed then.

so, do you leave it where it is?
nah, you move it.

you just don't move it anywhere.
that slot becomes vacant.

when you place all positive integers
you'd end up with every positive integer within range
mapped to their respective index.

and then you can reiterate.
the first gap you find, that index is the number you're looking for.

the first gap cannot be index `0` though.
slight concern.

consider

[_, 1, 2]

what would be the first gap that's not index `0`
in this case there's none.

so the answer should the the last number + 1

but what if the original list was [3, 1, 2]
the concept would've been move `3` to index `3`
but there's no index `3`, so it simply creats a gap.

a gap at it's original index, index 0
i think the point here, is to map each number to an index that's one less than it's value.

so you want to,
    map the number `1` to index `0`
    map the number `2` to index `1`

this way you've addressed the worst case where all the positive integers exist in the array.
this way if you don't find a gap, you know your answer is the last number + 1

and if you find a gap
you know your answer is `index + 1`

where do negative numbers go?
nowhere, you simply create a gap where they are.

same for numbers who don't have a corresponding index,
cause they're too big.

so the first iteration is the placement.
it'd be O(n) because i'd be moving `n` times.

what if you reach a value that needs no moving.
the telltale is `value == valueIdx - 1 `

the value is one more than it's index, for those ones i skip.
for the ones that do, i make a single move.

if i get to destination and see another number there.
i make another move.

it'd be a recursive move but every number only moves once.
this is the crux of the difficult explanation.

i have a sense why it should work.
but it's not crystal.

let's run an example

[3, 1, 2]

you start off with `3`
you realize it's not in the right index.

you want to move it.
where does it go?

it goes to the index that's one less than it's value.
`3-1` which would be index 2.

so, now the array is
[_, 1, 2]

we reach index 2 and meet the number `2`
what to do??

move it to it's own index.
which is index 1.

so, again, we create another gap
[_, 1, _]

keep in mind, we have two pending inserts.
the one at index 2
and the one at index 1

in both cases, we met another value there.
and so started another move.

we get to index 1.
we see a value there..

it's 1 and it should be at index 0

so, a third pending insert.
we reach index 0, we see it's blank.

so we resolve the first pending insert.
we have:

[1, _, _]

now we go back to index 1
and can now place number 2
[1, 2, _]

then go back to index 2
and can now place number 3.

[1, 2, 3]

in each case, each number only moves once.
the recursive calls handle any occupied cells.

but each of them are numbers and only move once.
this continues happening until we fill a gap or encounter a number that has no valid index.

either it's index would be out of bounds
or it's a negative number.

this is the sort of thing that would benefit from an `animation`


