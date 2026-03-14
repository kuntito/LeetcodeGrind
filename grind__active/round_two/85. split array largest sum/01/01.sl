# https://leetcode.com/problems/split-array-largest-sum/

i'm given two things.

a number and an array of numbers.

the array of numbers is called, `nums`.
the number is called, `k`.

i want to split `nums` into `k` parts.
and find the part with the largest sum.

the question is, how do i perform the split?
if `nums = [1, 2, 4]` and `k=2`

i could split in two ways:

[1, 2] and [4], OR
[1] and [2, 4]

so which one do i pick?
you want to pick the split that gives you the smaller largest sum.

in the first split,
[1, 2] and [4], the part with the largest sum is `[4]`

in the second split,
[1] and [2, 4], the part with the largest sum is [2 + 4] = `6`

of these two splits, the first split has the lower largest sum.

okay, what if there were more than one split?
it's still the same thing.

you'd explore every split, note the part with the largest sum.
then compare this with other splits and return the lowest one.

**
and how would this look like in code?

write the code and answer the questions as they come.

what you want, 

is to explore every way you can split `nums` into `k` parts.
and for each split, note the part with the largest sum.

and of all the largest sums, you find, return the smallest one.
