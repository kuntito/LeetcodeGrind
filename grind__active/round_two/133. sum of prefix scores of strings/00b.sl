i have a list of strings, `words`.
i want to return a list of numbers.

for each string, i want to find it's number.

what's the number?

for context,
each string has as many prefixes as characters.
a string with three characters, `abc`

it's prefixes are:
* a
* ab
* abc

now, we've established that.
to get the number of any string in `words`

we ask,
for each prefix of the current string.
how many strings in `words` share the same prefix.

re-using our example, `abc`

the first prefix, `a`
we ask, how many strings in `words` share this prefix?
same goes for `ab` and `abc`

the total across each prefix is the strings number.

let's write the first attempt.

# TODO TLE, rewrite.