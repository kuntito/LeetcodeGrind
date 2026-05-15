`populateCache`

what he does here is, iterate through the numbers in reverse.

at each index, explore how wide a split can get.

and for each split, 
it compares it's sum with another split sum.

and then, does some other things.

my concern with this approach is, it doesn't acknowledge the scenario
where the widest split is the only split.

when the split is `1`

and the split width is `5`

there's no need to explore widths 1 through 5.
only one split can be made at that point.

and that's the entire split.

and so just cache.

also, you don't have to iterate through every index.

perhaps, i'm addressing the wrong thing here.

the core of this is to find out why this works.

but i'd need to break it down in my way to see how it works.

staring at this code does nothing for me.

skipping ahead as well.

if i don't get it, i don't get it.

there's no shortcut to this joint.

only way is through.

so, what's the next concern?

why reverse through nums?

well, i think that's bottom-up.

address the last split then the one before it, then the one before it.

when addressing the second split, it still goes through from the last index.

well, it shouldn't.

if split is 2, then it should start from the second last index.

since that's how far a valid second split can travel.

so the way to go with this, is, for each split.
determine the valid range from behind.

so, the question'd be, for each split.
how many have passed? assume each further split was width 1
where would i end?

now, you know the end.

where would i start.
well, that's a function of how many other splits left.

assuming they were all width 1, that tells me my starting position.

now, i know the range for the second split.

and can now, run through the range, exploring every width.

when width is `1`, what's the next split like?
the cache knows.

when width is `2`, what's the next split like?
the cache knows.

so through the range exploration, i'd track the ...

track the what?
what exactly am i doing with the exploration?

thing is, i want to explore every width and determine the smallest max.

at split 2, each path is 2.

so each iteration, is me, exploring a path.

so what is the cache doing? storing the result for each path.

thing is, it compares each width sum, with the smallest max of -

actually, it doesn't.

it compares each width sum with the split sum of the next split starting after it.

for instance, we iterate through ranges...
yeah, say, seven elements in `nums`
we on second split, and going through (2, 5)

at width (2,), you're comparing with the split1 sum that starts at index 3
at width (2, 3,), you're comparing with the split1 sum that starts at index 4
at width (2, 3, 4), you're comparing with the split1 sum that starts at index 5
at width (2, 3, 4, 5), you're comparing with the split1 sum that starts at index 6

so the name `smallestMaxSumAlongRemainingPaths` might not be accurate.

i'd have to investigate.

with the way, this is written.

it raises the question if the cache needs the shape it has.

what's happening is we attend to each ordinal split in reverse.

the first split has several variations, and so we store them all in cache.

cache[i][1] = ?
cache[i+1][1] = ?
and as many more are needed.

so every version of the first split now exists in cache.

now, second split, we do the same.
explore every variation.

now, for each one we explore, we compare it with the split after it.
the first split.

we want to know which of them is bigger.

whichever is bigger, we cache that at:

cache[j][2] = the bigger one
cache[j + 1][2] = the bigger one

and so each position on the cache contains the max sum, along it's specific path?

actually, no.
the algo, does two things.

still on the second split.
first you compare the current split sum with the one that begins after it.

in this case, the one for split 1.

we determinew which is bigger.

then cache, but the cache doesn't cache which is bigger.

it caches, what's smaller between whatever already exists at the cache position
and this bigger value from the earlier comparison.

the cache positions are initialized to an inordinately high value, `float(inf)`
and so...

the smaller one ends up being the bigger number from the earlier comparison.

not entirely sure, why the cache is initialized to `float(inf)` when we only ever compare a single path for each position.

perhaps, for convenience?

let's explore the iterations a little more.

so, for the second split.
after going through each width, what would the cache look like.

well, since, the numbers are the rows, when you cache a result.
you access the row where the current split starts, and find the specific split you want.

so, if the first split accesses index 5, it'd store it's cache in the column idx 1.
now, if the second split also accesses index 5, it'd store it's cache in the same row, but column 2.

i don't see how a clash of positions occur.
where you'd need to a min between values.

but run the second split till then end.

what'd happen is every position on column index 2,
relevant to the second split's width is filled.

can i see this in practice.

i've seen how a clash would occur.

thing is, when exploring the different paths on different split widths.
you always cache on the starting point of split width.

is akin to asking, if i split width 1, what's the best i can get.

hold it.

if i split width 2, what's the best i can get?
if it's smaller than what i'm holding, hold that.

if i split at width 3, what's the smallest i can get?
if smaller than what i'm holding, hold that instead.

in essence, i'd only ever need to store the starting point for all widths.
to get the smallest max for any split.


my statement about getting the range of each split (starIdx, endRange) is incomplete.

what's happening is, for each split, we're determining the smallest max along all paths.

[1, 2, 3, 4, 5] 

way i thought about it was for split 2.
in a 3-way split.

i'd assume every split before and every split after was width 1.

that way, the second split can be at most

(2, 3, 4)

then the iterations go from (2,) to (2, 3) to (2, 3, 4)
which is valid.

what i didn't consider was, the second split could also shrink.
i've addressed every variation of the last split by expanding from
(2,) to (2, 3, 4),

however, the first split, starting at (1,)
can also grow...

and when it grows, it shrinks the second split/

and so, the second split can actually be (3, 4) or (4,)

this is the reason for the reverse iteration.
by going backwards, you address the situations where the current split shrinks.
once you reach the starting point, you address the situations where it expands.

the concern would be the way it's written currently.
there's some slight inefficiencies since the code iterates through the entire nums backwards

then does so forwards till it hits the end range.

so, it's
you go to `5`, there's nothing much to explore..
since the endRange is `5`

you go to `4`
you explore (4,) and what comes next.

you go to `3`
you explore (3,) and what comes next.
you explore (3, 4,) and what comes next.

you go to `2`
you explore (2,) and what comes next.
you explore (2, 3,) and what comes next.
you explore (2, 3, 4,) and what comes next.

and so.. you'd have explored every variation of the second split.

when laid out.. it's
(4,)
(3,)
(3, 4,)
(2,)
(2, 3,)
(2, 3, 4)

all valid splits.

the density of logic is crazy.
how was i post to see this from the jump?

does Navdeep even know this is what it does?
