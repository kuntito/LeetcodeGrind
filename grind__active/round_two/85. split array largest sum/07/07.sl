an overview of the algorithm, what am i doing?
i'm exploring different paths i can get `k` splits.

starting with the first split.
how many ways can i make this first split?

i explore each way.
for each way, i then find the second split.

how many ways can i make this second split.
it's recursive, but this approach doesn't look like it.

what it does is address each sequential split..
the first split, the second split, the third... until k splits..

but first it addresses the first split.
what happens here?

it iterates in reverse through `nums`
at each point, it asks, can the split be formed from here.

and then caches the result.

but a few things go on, in each reveres iteration.

for each index, you find out how much you can travel to form the current split.
and then explore every variation of that range.

for each variation, you're asking, what's the smallest max sum for the next split?
the cache ensures no additional work is done.

for the first split, there's no next split and so.. you'd get a zero.

however, the way it's written, you can make unnecessary checks.


`
    def populateCache(self, nums, splitsLeft, cache):
        numsLen = len(nums)
        
        for curIdx in range(numsLen - 1, -1, -1):
            curSum = 0
            
            endRange = numsLen - (splitsLeft - 1)
            for curNumIdx in range(curIdx, endRange):
                curSum += nums[curNumIdx]
                
                smallestMaxSumAlongRemainingPaths = self.getSmallestMaxAlongAllPaths(
                    curNumIdx + 1,
                    splitsLeft - 1,
                    cache,
                )
                
                maxB = max(
                    curSum, 
                    smallestMaxSumAlongRemainingPaths
                )
                
                cache[curIdx][splitsLeft] = min(
                    cache[curIdx][splitsLeft],
                    maxB
                )
`

i named it `populateCache` so it might not be a good summary, but the code is essentially neetcode's with renamed variables and untangled logic.

when dealing with the first split of any path.

we'd call this method, iterate from behind through `nums`.

say `nums` is [2, 7, 5]

we start off with the last index, value 5

then check it's range, it's range would be `3`, `endRange = numsLen - (splitsLeft - 1)`

which effectively translates to (5,)

we'd check the smallest max sum along remaining paths and get a zero.
it's been written such that when the current index goes out of bounds, you've addressed your last split and so, return `0`

there's no smallest max sum along remaining paths here.

now, going back to the reverse iteration through nums,
you'd be at the middle index, with value `7` then deduce the range as (7, 5,)

but what happens is you iterate through the range, picking each value
you pick the `7` and ask what's the smallest max sum along the remaining paths..

but you're at the first split...
you can't pick only `7`, you'd have to pick 7 and 5..
the algorithm handles it with the use of `inf` but it shouldn't even be the case.

less i'm bugging.

`TODO, continue this line of reasoning tomorrow`