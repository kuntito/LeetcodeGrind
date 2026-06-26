i want to return a list of strings.

after receiving two inputs.

***
i'm given two things.

a string, `s`.

and a group of strings, `words`.

i want to find out the different ways
i can break `s` into chunks.

such that each chunk exists in `words`.

and for every way, `s` can be broken.
i want to collect the chunks
as a single string,
where each chunk is separated by a space.

WHAT'S THE APPROACH?
it's feeling like a dp problem.

the question is what chunks begin at the start of `s`

say, s is `cinderella`
`c`, `ci`, `cin` are all chunks that begin at the start of `s`
whether they're in `words` is a different concern.

but for every chunk that exists in words,
you want to find the chunks that begin after it.

that's the sub problem.

you're repeating this step till you run out of characters.
at which point, you save the chunk order.

space separated string.

can you cache?

let me do it without.
then add the cache.