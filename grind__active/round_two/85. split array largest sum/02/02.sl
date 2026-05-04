# https://leetcode.com/problems/split-array-largest-sum/description/

i'm given an array.

i want to determine some information about it.

***

i'm given an array.
i want to find out some info about it's props.

***

i'm given an array, `nums`, and an integer `k`.

i'm told to split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is minimized.

and then return the minimized largest sum of the split.

but what on earth does this mean?

let's take it one a time.

i'm given an array, `nums`
i want to split `nums` into `k` non-empty subarrays.

the non-empty doesn't do much here.
the intuitive sense of splitting an array is non-empty.

and so, i can rephrase.

i want to split `nums` into sub-arrays.

what's a subarray.
a continuous chunk of elements from the array.

okay, so these chunks.

specifically, `k` chunks..

***

i'm given an array.

i want to split it into `k` chunks.

but i want to split it in such a way that the largest chunk is as small as can be.

but what does this mean?
there's several ways i can split the array into `k` chunks.

is there several ways?

well, depends on the array.


***

i'm given an array and want to split it into a certain number of chunks.

i want to split it such that the sum of the largest chunk

***

i'm given an array.

i want to split this array into several parts.

***

i'm given an array
i want to split it into `k` parts.

i want to split it such that the part with the largest sum is..

***

i'm given an array.
i want to split it into `k` parts.

but i want to split it such that the part with the largest sum is as small as possible.

how would this go?
i'd have to split it one way, to know the part with the largest sum.

or is there a way around this?
what if you only search the biggest chunks.

the biggest chunks are not guaranteed to have the largest sum.

consider the array:

[1, 1, 4] and we split into two parts this way:

[1, 1] and [4]

the biggest part is [1, 1], it has two items.
but the sum of that part is `2`

meanwhile, the smaller part [4], has a bigger sum.

so, biggest part is not necessarily enough to make a decision about the part with the largest sum.

what if we sort the array, so we can optimize the search with the sorted order.

the problem with that is, we'd be changing the start array.

the question demands we figure it out the way the array is presented to us.
also, sorting would mean, our chunks can become disjointed.

a chunk is a chunk, because the indices follow each other in the array.

so what do you say?

i say, i simply have to explore every way, i can split `nums` into k chunks.

for each way, i'd figure out the largest chunks.

to be fair, i simply need the sum for the largest chunks.

and return the smallest of the lot.

let's try it, see what happens.

it seems to work, besides the TLE.

my concern here is, is there any repeated work?

are there chunks i revisit more than once?

consider this:
[1, 2, 3, 4, 5]

when k is `3`

i could have:
[1] [2, 3] [4, 5]

and
[1, 2] [3] [4, 5]

in both cases i have [4, 5]
i'd have known the sum from the first attempt
so i wouldn't need to calculate it on the second attempt.

in other words, i can memoize chunk sums.

a hashmap for (startIdx, endIdx)

or really, a prefix sum would suffice.
one calculation once.

the prefix up till startIdx subtracted from the prefix up till endIndex
gives you the subarray sum.

nope, prefix sum, is not enough.

perhaps, there's something, i'm missing.

perhaps, i don't need to explore every split.

just every valid subarray window.

grab the sum, but how would you know if it's the largest.
the largest only reveals itself in each split.

time for NeetCode.

# TODO let's try this again tomorrow
# just watch the video: https://www.youtube.com/watch?v=YUF3_eBdzsk&t=330s