i want to split a string
such that every split is a palindrome.

i want to find the least amount of splits possible.

i explored every substring, and counted palindromes.
but it was inefficient.

and Claude pointed out.
at each index, you need not explore it onwards more than once.

each index, can be treated as it's own string.
and the question is, what's the least amount of splits,
i can get here?

going back to main string.
that's the same question you asked from the jump.

and what's the shape look like?
first character, is it a palindrome?

yes, then explore the rest of the string.
each exploration, should conclude it's answer.

take

`a`

single character, nothing to split.

i take `ab`

first, take `a`
then explore the rest.

`b`, single character.
nothing to split.


so, at index `0`
the least split is `1`

okay, let's consider, `aab`

if i take `a`
i'd have `ab`

then ask, `ab`, the least split would be `1`
for a and ab, the least split is ...

not sure i'm doing this right.
try again, later.