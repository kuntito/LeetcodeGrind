i want to return a number.

after receiving three inputs.

***

i have a list of words.

i have a list of letters.

and every character has a score.
every character of what?

the ones in the words.
or the letters themselves?

i want to return the maximum score
for any valid set of words.

what's a valid set of words?

***

had to stop writing and do a rethink.
looked at the example.

words = ["dog","cat","dad","good"]

letters = ["a","a","c","d","d","d","g","o","o"]

score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

answer = 23.

'pparently, we're dealing with the lowercase characters
of the English Alphabet.

every character has a score.

then, i'm given a group of random letters.
and a group of random words.

and i'm told to use the letters form the heaviest
group of words.

heavy is total score of letters in a word.
the group weight, is total score of letters in the group.

that total score is what i'd return.

***
now, how to solve?
picking the heaviest word first.
might not be the best attempt.

since picking that word,
could mean no other word can be formed.

meanwhile, picking a smaller word,
can result in a bigger group.
since, there's room for other words.

in essence, i'd have to explore every option.

feels like a dynamic programming question.

start from behind.

given one character.
what's the heaviest group i can form?

probably, zero.

then you move to the penultimate character.
given this character,
what's the heaviest group i can form?

and what would that mean.
could mean that character and the last character taken as a word.

or that character and the last character taken as individual words.
then whichever's bigger wins.

on to the second penultimate.
what's the heaviest group i can form here?

let's write it out.

`abc`

a + bc
a + b + c
ab + c
abc

thing is, i know the best i can do at bc.
so i need not do..

a + bc, AND a + b + c
the cache at bs index holds this info.

what i don't know is ab + c
i'd need to do, ab, THEN use cs cache

then do abc.

seems like..
for each chunk for words.
i'd iterate, increasing the subChunk and using the cache.

bestScore = 0
slice = ""
for idx, ch in enumerate(chars):
    slice += ch
    thisScore = slice + getCache(idx)

    bestScore = max(
        bestScore,
        thisScore
    )

TODO let's carry on from here, next time.