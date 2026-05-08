so the question is, what is res?

what are we doing?
what am i doing?

for each iteration, i'm going through every way i can take the current split.

narrowed down, i'm only taking one split per time.

so, each iteration, rather each function.

i'd take a split, start another function
take a split, start another function,
take a split...

i'd keep going till i've taken all splits
then what, what do i return.

the base case, is worth understanding.

at the time you run out of splits, 
you do so in a recursive function.

in it's own recursive function.

cause, way it works is, for every split you take,
you attempt taking a split from next index

and you do that in a recursive call.

and so, the base case would be one where the travelling index 
is out of bounds

and at that point, you return what?

the return is based on what you've defined in the recursive fn.

what are you trying to return for each function?

off the dome, it seems the smallest-
to be fair, it's not clear.

zooming out far enough, it's the smallest of the largest splits from all paths.

however, when considering a single path,
what does res mean..

let's address `maxHereOnwards` first

once we hit the base case, run of index, we return 0

this goes back to meet the last split sum

and we compare the split sum with the return 0

which one of these is larger?

you pick the larger one.

what is this attemptiong to do?

finding the larger split from that point onwards.

now, what we do next?

is find what's smaller between res and the larger split.

the larger split would be the last split sum since the base case returned 0.

but the res comparison?

res is initially, float("inf")

the biggest float we wouldn't reach

and so i find which is smaller 'tween res and the last split sum

in this case the last split sum.

so that value belongs in res.

what do i do then..

i'm still within the iteration..
if there's another split sum, i can explore, i do so.

actually, i can't. if i hit the base case, it must mean
the last split was the last.

to really, deep this.

consider a situation where you're picking the last split.
and there's two ways to do it..

actually, there isn't but the algo is written such that you explore every way.

say your last split is of size 2.

algo's written such that you iterate through the first size, get the sum, recurse
then both sizes, get the sum, recurse..

when you get the first size sum, then recurse..
last index isn't out of bounds

but you've run out of splits.

and what do we do, return float("inf")

what does this do for us...
well, we'd compare, what's bigger between.. float("inf") and the split sum of size `1`

and take float("inf")

then compare this float("inf") with res..
which is also, float("inf")

and so, we'd have float("inf")

i'd say the whole point of that returning that float, is so res stays the same.

if res was float, nothing changes.
if res was less, since we do a min, nothing changes.

how about the max.. before the res min..
for that, we also don't touch it.

because it's a max, float("inf") would always win
and when you compare that with res, res would always win.

so it's a property that does nothing
way the algo is defined,

and it shouldn't do nothing, since that case is invalid.
we've made all splits and there's still items left.

we've made more splits that we should.
that path is inaccurate.

next, we get size 2 and do the sum, recurse, get 0.

get what's bigger, copare with res.
get what's smaller.

in the case of the final split, there's no where i'm getting a different res.

really, the final split should just be, sum up the entire index values

compare that with, you actually don't need to compare it with nothing.
for max...

simply get the sum, compare with res on a `min` level
then get what's smaller.

no need for iteration on the final split.

but still this doesn't tell me why the algo works.

say i need two splits and hella numbers in the array.

the first split has variations, the next one doesn't.
so i'd run through each variation, then grab the next one.

in this case, i'd have two split sums.
for each iteration, i want to know the bigger one.

the compare that against the `smallestMaxSum`, in the first instance
this value is float inf.

so whatever the first variation plus final split is, wins.

now, i take another variation, get the final split.
find the bigger one..then.. compare with `smallestMaxSum`

now, what am i doing, with this step.

at this point, i'm running two functions.

the first one spawns the second.

fn 1, fn 2
fn 1a, fn2b

when fn2 returns a value to fn 1
i compare the sums of fn1 and fn2, which is bigger.

this tells, me the split with the max sum along that path.

once, i know that, i can discard the value.
actually, i track the smallest max sum i've seen.

at this point, i've only seen one.
so that's the guy i track.

then fn 1a and fn2b
i compare the value of their sums too, which is bigger.
now, this number represents the biggest sum along a different path.

now, i compare this path with the smallest max sum i've seen.
the result from last iteration.

and then, that value holds the smallest max sum along the two paths it's seen.


okay, consider:
[2, 4, 3]

there's only two ways to split
*   [2], [4, 3]
AND
*   [2, 4], [3] 

in the first case, the max split sum is [4, 3], `7`
the second case, the max split sum is [2, 4], `6`

res holds on to `6`, discards `7`

now, the question is, what if the path with `6`
has a larger previous sum?

what do you mean, say i introduce an `8` and increase the number of splits to three.

we started with [2, 4, 3]

now, i'm saying [8] + [2, 4, 3]

i think the issue here, is the `8` applies to both split paths.

if i've said, isolating [2, 4, 3], the smallest split sum is `6`
if there's a bigger number before it that eclipses, `6`, and changes the final result.

it would also do the same for `7`
since they're operating on the same principles.

so it'd be a situation of comparing `8` with `6`
which is bigger, the 8

then comparing this with the smallestMaxSum at that point.
it never sees the 7, it didn't need to.

if it did, it wouldn't change the result.

the recursion summarise.

of all the paths that can be generated here.
what's the smallestMax sum.

you return that.

the parent call is asking the same question.

if i pick 8, what's the smallest max in the remaining.
you store the value in smallestMaxSum.

next question, if i pick [8, 2], what's the smallest max sum in the remainder

i do the comparisons.

so each function takes care of it's own.
***
TODO start here, what you did was pass max sum along each path to every recursive call.
i'd need some time to dive deep into this, and compare how it's different from Neet's.

till tomorrow.