i have a list of strings, `words`
i want to return a list of integers.

***
for each string,
i want to determine it's number.

and return an array of these numbers.

what is this number?
it's the number of strings in `words`
that have a prefix of the current string.

what do you mean?
say you have three strings.

["ma", "bro", "madrid"]

for each string,
you want to determine it's number.

you'd start with,
"ma"

it's number is how many strings in `words`
begin with "ma".

in our case, two.
"ma" and "madrid"

so it's number is `2`

you do the same for "bro"
how many strings in `words` have the prefix "bro"
just one.

"bro"

so, we'd have `1`

same goes for "madrid", it's number is `1`
your result is [2, 1, 1]

***
`i've completely missed the plot.`
