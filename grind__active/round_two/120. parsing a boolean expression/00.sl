# https://leetcode.com/problems/parsing-a-boolean-expression/description/

i'm given a string and want to return a boolean.

i'm told the string represents a boolean expression.
but what does that mean?

scratch the boolean expression description.
i'm given a string, the characters within, combine to a boolean.

i want to find that boolean and return it.

the starting point is what are the characters within the string.

for one, i have the characters: `t` and `f`
`t` represents True
`f` represents False

then i have the combination of characters.
an exclamation mark followed by parenthesis
`!()`

whatever's within the parenthesis is also a similar string.
one that evaluates into a boolean.

and the exclamation outside the parenthesis negates it.

then it seems i have more character combinations like this.
i have an ampersand outside parenthesis `&()` and
a vertical bar followed by parenthesis `|()`

these two are similar, the outer character `&` and `|` act on the contents of the parentheses.

however, for these two, the content of the parentheses are comma separated boolean strings.

i.e. `&(f, t)` or `|(t, f)` 

and what these mean is, for ampersand, `&`, it means AND all the expressions within the parenthesis.

and the vertical bar, `|`, means OR all the expression within the parenthesis.

i'm told the given string is valid. it resolves to a boolean.

i should find this.

and how would i approach this?

well you want to start from the innermost parentheses, resolve the expression, then expand outwards.

and if there's no innermost parentheses?
or if there's several innermost parentheses, what do you do?

these are separate problems, it's worth treating them as such.
if there's no innermost parenthesis, what do i do?
what does that look like?

for one, it means there are no parentheses.
by extension, no vertical pipe, no ampersand and no exclamation mark

i'm left with a `t` or an `f`.

the question doesn't say i can have `tf` or an `ft`
so i'd assume this is not the case.

`in other words, if i have a single character, it's a `t` or an `f`
i can resolve this individually.`

next up, if there's several innermost parentheses, what do i do?
well, nothing changes.

i'd still address all at the same time.

resolve the innermost ones, look at the shape of the problem again.
the solve.

for the lay man approach.
i'd run through the string.

track every opening parentheses and order it.
i could use a min heap to store the order.

this way, i can know the deepest opening parentheses at a glance.
along with the order, i can store the index.

every opening parenthesis has an end one.
i can pair them too.

so the min heap item would be (order, openingIndex, closingIndx)
with this i can solve the smallest opening parentheses.

or several of them if they exist.

well, solving them isn't the core of this problem.
it's what you do after.

say you solve the opening parenthesis, what do you do next?

you'd have a new string, and want to address that.

how about i don't solve the innermost one, all at once.

if i have two innermost parentheses, solving one, doesn't mean i ignore the other.

the way it'd go is, i'd run a pass on the string.

find the innermost paren, resolve it.
replace the slice from the `parenStartIndex` till the `parenEndIndex + 1` with the resolution.

the reapply the same algo on the new string.
once you repeatedly do this, you'd resolve every parentheses until you have a string with a single character.

in which case you can simply return it.

the main function can recurse on itself.