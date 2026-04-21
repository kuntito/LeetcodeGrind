# https://leetcode.com/problems/trapping-rain-water/description/

i'm given an array of integers.

i'm told each integer represents the height of a pillar.
if a depression exists between pillars, i can store water in it.

my job is to find out how much water can be stored.

what does a depression look like?

[2, 1, 3]

at pillar `1`, i have a depression, 
since the pillars next to it are both taller than it.

and how much water can be stored there?
the depression is only one unit deep.

where did one unit come from?
well the pillars to it's left is `2`
the pillar to it's right is `3`

if i filled the depression at `1` with water
the highest it can rise is pillar `2`

hence, the depression is always limited by the shorter pillar.

this is the first insight, or rather two insights.

to store water, you need the adjacent pillars to be taller than your current pillar.
and the amount of water you can store is a measure of the shorter of the adjacent pillars.

so, at each pillar, the question becomes...
becomes what?

what's the pillar to my left?
what's the pillar to my right?

no, not exactly.

consider:
[3, 2, 1, 3]

say i'm at pillar `1`
my immediate left is `2`
my immediate right is `3`

my writing so far suggests the pillar `2` is the limiting factor since it's the shorter pillar.

but merely looking at it, i can keep filling water, since the water would overflow past the pillar `2` and be capped by the pillar `3` on the extreme left.

so really, the question at each point is what's the tallest pillar to my left?
what's the tallest pillar to my right.

the shorter of those pillars minus my height determines how much water can be stored at this position.

i can track the tallest left pillar as i iterate through, but the tallest right?
i'd have to search?

one on hand, i can search once and store the tallest right pillar for every index
and i'd have the ingredients for a solution.

this would be O(n) time and O(1) space.

however, Navdeep Singh says he's got an O(1) space solution and that's what i want to explore.