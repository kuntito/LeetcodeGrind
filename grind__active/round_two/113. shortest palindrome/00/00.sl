# https://leetcode.com/problems/shortest-palindrome/description/

i'm given a string, `s`

i want to turn it into a palindrome.

to do this, i'd add characters to the start of the string.

the idea is to attain a palindrome using the least amount of characters possible.

what would this look like?

the least number of characters i can add is one.

if i add one character to the start of the string.
it'd have to match the last character in `s`.

then the question becomes, is this new string a palindrome?
truth is, i can't say unless i check.

if it is a palindrome, i'd return the string.

if not, i'd add another character.
but which one?

let's make this plain.

i'm starting off with `abc`

what am i doing here?
i'd add a `c` to the start, it becomes `cabc`

it's not a palindrome.
so, what do i do?

now, what, i'd have to add another character
but which one? the second last character.
`b`

do i add this to the front of the string?
well yeah, but the front of `s` not the modified string.

it's basically, with every character you add
to the front of `s`, the next characters push the existing ones leftward.

but how does this help you solve the problem?

***

let's take another swipe.
given the string `s`

it's either a palindrome or an incomplete palindrome
from the jump.

if i check `s` as is. is this a palindrome?
if yes, i'd return `s`.

else, i'd add a character to the start.

***

how about this? a palindrome is either even or odd lengthed.
i can check if a string is a palindrome from the middle then expand outwards.

with every character i add to the start of the string.
i'd trigger another check.

and how would this work?
two data structures.

an array for the characters i'd add.
the string, `s`

together, i can tell the length of the modified string.
if i know the length, i know the middle.

if i know the middle, i can expand.

if i can expand, i can check for palindrome.