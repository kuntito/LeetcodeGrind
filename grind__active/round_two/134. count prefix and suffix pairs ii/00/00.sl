i'm given a list of strings and want to return an integer.

from the list, 
i want to find the number of string pairs that meet a condition.

what's the condition?
well, there's a couple.

first condition,
    the two strings forming the pair must be at different positions in the list.
    let's call the string that appears first, `firstPosStr` 
    and the other one, `secondPosStr`

second condition,
    the `firstPosStr` must be a prefix and a suffix of the `secondPosStr`

WHAT TO DO?

well, grab every pair and check.

TLE.

how to make efficient?

any repeated work?
well, let's dive into it.

what's going on?
you take one string, compare with another.

you'd have to explore every pair to know if they meet the condition.
well, true.

except, there's duplicates.

what do you mean?

consider the list

`a`
`a`
`aba`

two valid pairs, 
the first `a` and `aba`
the second `a` and `aba`

and how could i avoid the double work?

convert the list into a dictionary.
that way, you summarise the duplicates.

then what?
you'd still explore every pair.

it's just the pairs are unique.
and i'd factor the amount of each string i have in the array.

if you had two `a`s and one `aba`
and they match
what does that mean,
multiply the frequencies of both numbers.

2 x 1

meaning two pairs.

if you had two of each...
do you multiply.

well, not exactly.
the concern here, is the order of the strings.

if `aba` came before `a`
we can't use that pair.

since `aba` is not a prefix/suffix of `a`

it doesn't work.

a rewrite? yes.

