i have a queue of people.

i want to answer yes or no.

i want to know if the people are queued according to their heights.
i can also remove one person to make them line up according to their heights.

so, what's the crux of this?
well, are they lined up according to heights?

if yes, your answer has arrived.

if not, can i remove one person
so they line up?

well, what would this look like?
i'd say, look from the start of the line.

is the next person at least the same height.
the first short guy i find, i remove.

`4, 1, 2`

but, peep this.

if i start at `4`, `1` is a short guy.
if i remove `1`, i'm left with

`4, 2`, which is still invalid.

removing the first short guy is not a good strategy,
in this case, it'd have been better, if i removed `4`

then i'd have `1, 2`

how about this, find the first pair
that line up.

once you have that.
go left, and go right.

actually, that's two much.

if the array is less than three people.
yes, they can line up.
at most, i'd remove one guy.

if they're three people.
one of this is true.

if the people can be lined up.

either `the first and second person line up`.

or `the second and third person line up`.

if the first and second line up.
you keep going and seek the imposter.
if you find more than one imposter game over.

you'd do the same for second and third.
but it's feeling like i can do it in one go.

a two man window.
i check both men.

are they lined up.
if not.

i note an imposter.
then i check the next two men.
do they lineup.

if yes, i keep going.

if the window reaches the end without a problem.
i'm good.

so,

412,

checks 41, doesn't lineup, notes one imposter.
checks 12, lines up.

iteration ends, only one imposter was found.
so, yes, the people can lineup.

lemme write it, see what happens.

it fails this test case.
`[3,4,2,3]`


the imposter pair would be `42`

but clearly removing either number produces `323` or `343`
none of which line up.

i think the concern, is i also have to track the lowest seen.
so, at `42`, i have one imposter.

but another imposter is if one of the numbers is lower than the lowest seen so far.

but what if you pick the wrong lower number?
what does that mean?

not sure what i mean. lower is always better.
fair.

let's write it, see how it goes.

it didn't go so well.    

