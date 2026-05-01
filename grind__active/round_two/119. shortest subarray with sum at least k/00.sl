# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

i'm given an array of integers called `nums`.
***
i'm given two things.

an array of integers called `nums` and an integer, `k`.
what do i want to do with them?

i want to find the length of a subarray.

what subarray?
the shortest subarray with a sum of at least `k`.

the question does say, the shortest non-empty subarray with said sum.
however, i have omitted it from the breakdown since, `k` is guaranteed to be at least `1`

so any matching subarray can not be empty by definition.
at worse, there's no subarray that meets the condition.

now, that we're clear on things.
what do i do?

it's giving sliding window.
for each item in `nums`, create a sliding window
track the sum of the window

the moment you reach or exceed `k` in length
move the start of the window forward.

it's sounds a bit dodgy, particularly cause i just reached out for sliding window and didn't walk my way to it.

***
REWRITE and DO IT CLEARLY!