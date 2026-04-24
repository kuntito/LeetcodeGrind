# https://leetcode.com/problems/sliding-window-maximum/description/

i'm given an array of integers, `nums`

i want to iterate through `nums`.
but rather than iterate and pick one number at a time.

at each number, i'd consider the first `k` numbers after it.

***

i'm given an array of integers, `nums`

i want to iterate through `nums`, in groups of `k`.

what does this mean?
for every number in `nums`, i want to consider the first `k` numbers, starting from that number.

let's consider the array:
[1, 2, 3]

your typical iteration is this:
`1` then `2` then `3`

you go through each number and pick one.

for this question, i want to go through each number and pick `k`

using the same array:
[1, 2, 3], if k is 2

the iteration becomes:
    [1, 2] then [2, 3]

***
i'm given an array of integers, `nums`.

i want to iterate through `nums`, 
at each step, i want to consider the first `k` numbers.

consider this:
nums = [10, 2, 18]
k = 2

at each step, i want to pick the first two numbers.
at step 1,
    i'd consider the first two numbers [10, 2]
at step 2,
    i'd consider the first two numbers [2, 18]
at step 3,
    i'd consider the first two numbers.
    however, there's only one number, so the iteration can't have a successful step 3
    so nothing happens here.

***
i'm given an array of integers, `nums`

i want to iterate through `nums`.
at each index, i want to consider `k` consecutive numbers.

for instance, if nums is [10, 2, 18] and k is 2

at index 0,
    i'd consider 2 consecutive numbers, [10, 2]
at index 1,
    i'd consider 2 consecutive numbers, [2, 18]
at index 2,
    i'd consider 2 consecutive numbers
    but there's only one number.
    so i can't proceed with index 3.

***
i'm given an array of integers, `nums`

i want to iterate through `nums`
at each index, 
i'd consider `k` consecutive numbers starting at that index.

for instance, if nums is [10, 2, 18] and k is 2

at index 0,
    the two consecutive numbers would be 10 and 2
at index 1,
    the two consecutive numbers would be 2 and 18
at index 2,
    there are no two consecutive numbers
    only 18 is left.

    and so, i can't work with index 2.
    the iteration ends with index 1.

