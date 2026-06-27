i want to return a list of strings.

after receiving two inputs.

***

i have a grid of characters, `board`.

i have a group of words, `words`.

from the group,
i want to identify what words
can be formed by connecting the characters on the board.

the characters can only be connected vertically
or horizontally.

HOW TO SOLVE?

explore the board.

rather, explore the board at cells
where the character could start a word.

what do you mean could start?
if the character starts any of the words in `words`

and if it does,
you check it's verticals and horizontals.

for?..

it feels recursive.

at each point,
you have a character.
and you have a group of words.

does the character start any of those words?
if yes,
for all of those words, start another function.

in each function,
we repeat the same process.

a character,
a group of words.

difference now, is the character,
is the next character from the matching word we found in the last function.

and the group of words is the matching word minus the first character.

what's the idea?

create a structure.

it takes a group of words, returns a dictionary.
of character => words.

this speeds up the check.
but as we speak,
we'd need to do this for every matching first word.

fair but it's a start.

let's go.

