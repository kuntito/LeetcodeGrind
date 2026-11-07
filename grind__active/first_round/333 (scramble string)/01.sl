i'm given two strings.

i'm told one might be a scrambled version of the other.

i want to find out.

scrambling in this context is unique.

a scramble is, you take a string.
split into two substrings.

if the strings have less than 2 characters
they can't be split.

once you split,
each substring becomes it's own substring.

and you split that too.
in essence, you keep splitting till you hit
a substring with one character.

then what.
you re-combine the splits.

at it's basest,
you'd have

`firstSplit` and `secondSplit`

you can join them as `firstSplit + secondSplit`
of `secondSplit + firstSplit`

this is how scrambling happens.
so, how do i know if a string is a scrambled version
of the next.

well, i'd say explore every scrambled position.
see if any matches the other string.

then see a way to make it efficient.

yeah, i didn't discuss how i'd collate the string back together.
each exploration ends when it hits a single character.
but you want to get all the single characters.

let's walk through an example.

"ab"

i split, at "a"

i go in, i can't go any further.
what then.

i get back a.
in the same scope, i'd get back b.

then what, i want to combine as 

`ab` and `ba`

so, what i am doing, for each substring.
split, so i split at a

and got back the parts.
what i get is the parts.

then on each get back, i combine
one way and another.

then what?

it's not clear since it's the base case for this example.

okay, let's try

"abc"

okay, so i split at "a" and "bc"

i'd get back "a"
and at "bc", i'd end up with "bc" and "cb"

and "a" needs to know both.

so each exploration returns an array.

where for each character in the first split.
combine with the second split.

so, i'd have "abc"

and "acb"

then what?

return those too.
well, no, you're mid exploration.
you simply want to say you found them.

so "abc" scrambled gives you "abc" or "acb"
and this is the list that reveals if the the other string is contained in it.

yeah, that works.

hold on "a" returns ["a"]?

and "bc" returns ["bc", "cb"]
how do these form.

well b returns ["b"]
and c returns ["c"]

you're not iterating, are you?

you are, you're kinda doing both

a function returns a list of all it's scramblings.

explore every scramble pair.
and for each one, combine front and back.

and keep that in a return array.

it works, but memory limit exceeded
rightfull so..

# SECOND ATTEMPT
the thing is, a scramble string still has two parts.
even if each individual part is scrambled.

so, the first character of the second string,
you what half you're dealing with.

does it?

well, take the first character in the second string.

find it in the first string.
wherever it is, is the split.

and if it's the first character.
then you need to find where it ends?

what do we know of a valid second string.
the idea is it's first character and second character must be in
different parts of the second string.

but i don't know which part.
if i pick the start character, find it.
pick the end character find it.
what does that tell me.

well,
if the first character is before the second character.
then if the string is valid.
the position of the second character is where the split starts.

and you can treat each half as it's own recursive function.
okay, and if the first character is after the second character.
then if the string is valid.

the first character tells you the second part.
i see.

the simplest case is "ab"

"a" comes first, hence the second half is "b"

and if it were "ba"
the second half would be "a"

so, what's the end goal here?

if i have "ab" and second string is "bc"

i'd pair "a" with "c"
then pair "b" with "b"

in which case,

a doesn't match c.
okay, that's the base case.

when down to one character each, do they match.
if they don't you know your answer.

let's take another crack at this.

TODO start here...
yeah, i'd need another attempt at this.
a second string with `abcda`
doesn't tell you which `a` belongs where in the first string.


