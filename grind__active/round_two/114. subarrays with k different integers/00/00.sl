# https://leetcode.com/problems/subarrays-with-k-different-integers/

first, i checked the shape of the inputs.

`
class Solution:
    def subarraysWithKDistinct(
        self,
        nums: List[int],
        k: int
    ) -> int:
`

i'm taking two things and turning into one.

***

i'm given two things, an array and a number.

the array is an integer array called `nums`
the number is called `k`.

***

i'm given two things, an array of integers and a number.

the array of integers is called `nums`.
the number is called `k`.

my job is to find the number of subarrays within `nums` that meet a certain condition.
what's the condition?

the subarray-
what's a subarray?

a subarray is a list of back to back elements within `nums`
for instance, if `nums` is [4, 1, 3]

a subarray can be the 4 and 1, i.e. [4, 1]
since 4 and 1 occur back to back within `nums`

a subarray can also be 1 and 3,
since 1 and 3 occur back to back within `nums`

a subarray can also be 4, 1, and 3
yes, the entire array can be a subarray of itself

and lastly,
a subarray can be a single element.

[4], [1] and [3] are individual subarrays.

now, that we know what a subarray is, what's the condition that makes a subarray worthy of consideration?

the subarray must contain `k` unique integers.

okay, so we want to count the number of subarrays that contain `k` unique integers.

one way to go, is to explore every subarray, and check if it has `k` unique integers.
that's bound to cause a TLE, but i'd try nonetheless.

why optimize when i don't know if it fails yet.

it runs and TLE, rightfully so.
time to rewrite.