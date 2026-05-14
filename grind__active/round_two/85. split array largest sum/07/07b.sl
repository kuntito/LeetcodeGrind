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