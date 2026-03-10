i have two strings.

let's call them, `mainString` and `searchString`

i want to find the smallest substring in `searchString`
that contains every character in `mainString`.

*
/* 
and how would this go? 
i'd have to check the characters within `searchString`
and take note of what i want.

what do you want?
the smallest substring in `searchString` that has all the characters in `mainString`.

okay, say you start with the first character in `searchString`
it's one of two things.

either, it's in `mainString` or it is not.

+   if it is, what do we do? well, we move on to the next character
+   if it isn't, we move on to the next character.

well, you've used the same move in two contexts. is that correct?
no, it isn't.

in the first case,
    we note the character we've seen
    then we move on.

in the second case, where there's no matching character.
    we simply move on.

so the first case is what we want to explore.
we find a character that's in `mainString`.

we note it somehow and move on.

now, we're at a different character, with the same question.

is this character in `mainString` or not?

+   if it is, we note it, and move on.
+   if it isn't, we simply move on.

it's apparent, every step at this point is one of two things.
noting a character is in `mainString` then moving on.
or simply, moving on.

and when does it end?
it ends when we find a character from `mainString` that completes the character set, we've noted.

at that point, what do we do?
we would have found a valid substring.

so, we track the length of the substring.

but what next? do we keep moving?
we could but that would only lengthen the substring.

we want to find a shorter one.
so it makes sense to shrink the substring.

but by how much?
we keep removing characters from the start until the substring is no longer valid.

this removal would also un-note any characters we might have noted.
then we continue the iteration.

repeating the same steps until we find another valid substring.

and i've slightly misread the question. we don't need the length of the substring.
we need the actual substring.

it's solvable.

how would i summarise? */

*
starting with the first character in `searchString`
the first character that also exists in `mainString`

starting from that character,
i want to form a substring.

i'd continue the iteration, adding characters
until i get to a point where the substring contains all the characters in `mainString`

i'd store that substring somewhere.
then shrink the substring i'm iterating with.

shrink from the left until i'm back at the starting conditions.

"the first character in `searchString` that also exists in `mainString`"
however, it's practically the second -



