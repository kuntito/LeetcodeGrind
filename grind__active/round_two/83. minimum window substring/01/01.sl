# https://leetcode.com/problems/minimum-window-substring/description/


i'm given two strings, `s` and `t`.

i want to find the smallest substring of `s`
that contains all the characters in `t`.

if such a substring exists, there's only one of it's kind within `s`.
and, if no such substring exists, i should return ""

so how would this work?

first thing comes to mind is, iterate through `s`
check if all the characters of `t` exist within it.

if it does, shrink `s` until you find the smallest substring where
the characters still exist.

and if the first iteration reveals you can't find all of t's characters in `s`
return an empty string, `""`

okay, and how would the shrinking work?
i can start from either end of `s`

say i start from the left, i'd remove one character and ask
is the condition still valid, if yes, i'd recompute the smallest window substring.

if no?..
i think this is how i should decide what side to shrink.

i can't actually shrink from any end.
i always want to shrink from the end that's inconsequential to meeting the condition.

and what if both of them are inconsequential?
then, i'd have to test both scenarios.

i know where this is going, but i don't want to follow it.
shrinking from either side would lead to hella work.

it comes to mind first cause it's most intuitive.

the answer, i know.
but how to work my way to it, is what i don't.

another approach is for every t's character, i find in `s`
i can keep checking to see if that character is the starting point for the smallest substring.

i'd keep appending or rather tracking characters till i find all the characters in `t`
the moment i do, what happens?

is that my result? well, that is a result, whose it is, is what's unclear.

the only thing, i can say at that point is the substring i have found contains all the characters of `t`

can it be smaller? is that the question i'm asking?

going this route is a tad complicated.
the point i'm trying to make is for every of t's character in `s`
i want to track every character onward until i meet the requirement.

once, i do, i store the string i've tracked so far.
if it's the smallest, i update the smallest.

if not, i do the same for the next t's character in `s`
the next t's character in `s` would probably be in the substring i just tracked.

unless, `t` is a single character, in which case, i can simply return `t` if `t in s`

my concern is for when `t` is two or more characters.
so, the first substring is a measure of the first t-character i find.

then i move to the next.
in essence, i'm hopping through t's characters within the string.

the smallest substring, if it exists, must start from one of those characters
and i'd keep going till i find it, else, return `""`
