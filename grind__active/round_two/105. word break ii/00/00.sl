i'm given two things.

a long string, `s`
and a group of strings, `wordDict`

i want to find out if i can break `s` into smaller strings such that all the smaller strings exist in `wordDict`.

for instance:

s = "nastyjay"
wordDict = ["nas", "nasty", "ty", "jay"]

i can break up `s` into
"nasty" and "jay"

both words exist in `wordDict`

i can also break up `s` into
"nas" "ty" and "jay"

and all words exist in `wordDict`

for each way, `s` can be broken
i want to add a space in-between the smaller parts
so "nasty" and "jay" becomes "nasty jay"

"nas", "ty" and "jay" becoomes "nas ty jay"

and then i'd return a list of these joined strings.
i.e. [
    "nasty jay",
    "nas ty jay",
]

*** 
and how would this work in code?

i'd have to start from the first character in `s`.

what do you mean?

if i'm breaking `s` into smaller strings.
the first substring must start with the first character in `s`
but what if the first character isn't in `wordDict`

then we check the first two characters in `s`
at some point, i'd find a match or i don't.

if i don't find a match, it means, there's no way to break `s`
so the smaller strings are in `wordDict`

but if i do find a match, what happens?
the question now becomes, can i break the rest of the string into smaller strings such that the smaller strings exist in `wordDict`?

that's exactly the problem i started with.
so recursion.

in each step, iterate through the string, find the first substring that exists in `wordDict`, once you do, start another recursive function.

i'd need a array to track the substrings i've found.
the array would be passed to the recursive function.

so it can store all the strings.

the end case would be when i run out of words.
the substring should be ""

so i go back, i backtrack, i'd remove the word i found from the `trackingArr`
then see if i match any other substring.

the base case is where i add a space in-between the words in tracking array.
and i can add them to a global `resultArray`