# https://leetcode.com/problems/subarrays-with-k-different-integers/description/

what's the situation?

i'm given two things, an array of integers, `nums`, and a number, `k`.

i want to find the number of subarrays within `nums` that have `k` unique integers.

the first attempt had me running through every subarray and assessing them for `k` unique integers.

leetcode deemed it inefficient.

now, i have to improve the algorithm.

what's the way to go about this?

for one, your first sub array is going to start somewhere.

it must start somewhere.

it must start from the beginning of the array.
think about it.

what's the worst case? the entire array doesn't have `k` unique integers.
in which case, your answer would be zero.

what's the next worst case? say `k` is 2, and you have duplicates from the first element till the penultimate one.

your first subarray would still have to start from the first element.
however many duplicates, as long as another number makes it unique, the first element is valid.

and so, i can start the first subarray from the first elements.
i'd keep tracking new elements until i find `k` unique elements.

at which point, i'd have to do something. but what?

consider when nums is [5, 5, 3] and k is 2
i'd start the subarray at index 0 and end it at index 2

i have my first subarray.
what does that mean?
can i disregard the first element?

yes, i can.
so i'd disregard it and move the start of the subarray one step forward.
now, i'd have [5, 3]

i still have a valid subarray, so i can increment my valid subarray count by one.

i'd move the start of the subarray one step forward and be left with
[3], at this point, i no longer have a valid subarray and so, i don't increment.

i continue adding elements to the subarray, but really, there's no more elements to add.
i'm at the end of the subarray.

it works for this example, but i doubt it will for this.
consider when nums is [1, 2, 1, 2, 3] and k = 2

off the glance, i can tell, [1, 2, 1] is a valid subarray.
however, with my algo..

i'd start of with the first elements, append elements until unique count is `2`
the first point of this would be [1, 2]

then i increment the start of my subarray, it becomes [.., 2]
then add more elements till i hit the `k` count

my next stop is [2, 1]
which is also a valid subarray.

however, it's apparent, that i'd have skipped the case of [1, 2, 1]
and so my algo fails.

simply because, i find `k` elements doesn't mean i should shift the first element forward. i should actually keep going until the `k` condition is no longer true.

but there's also merit in shrinking from the start of the subarray.
consider when i hit the stop, `[1, 2, 1]` and k is `2`

the next element is `2`, an element that already exists. so there's value in continuing since, i'd get `[1, 2, 1, 2]`.

but there's also value in shrinking, so i'd get, `[2, 1]`

i think i see the shape of the solution.
from the jump, i'd start with the first elements, tracking new ones until i hit `k` unique elements.

actually, i keep tracking. when i hit `k` unique elements.
i'd start a recursive call where i remove the first element.

this way i'm effectively creating a branch where i've travelled up till my destination,
but skipping the first element of my current subarray.

if the condition is still true, i'd start another recursive call.

i'd essentially keep going till i no longer have `k` unique elements then climb up the recursive stack.

let's walk through the example again.
nums is [1, 2, 1, 2, 3] and k is 2

i start off and hit [1, 2], `i increment count`
i start a recursive call with [2], it ends there since the condition is not met.

i go back up the stack, continue interation,
i hit [1, 2, 1], `i increment count`
start a recursive call with [2, 1], it's valid, `i increment count`
since, it's valid, i start another recursive call with [1], recursion ends there.
i go back up two stacks and continue iteration.

i hit [1, 2, 1, 2], `i increment count`
recursive with [2, 1, 2], `i increment count`
recursive with [1, 2], `increment count`
recursive ends.

go back up stack.

i hit [1, 2, 1, 2, 3], but this is invalid
i move the front of the subarray forward until it becomes valid again.

[_, _, _, 2, 3]

it doesn't happen till i hit [2, 3]
at which point, `i increment count`
recursive with [3], it don't work.
i go back up stack.

at this point, no more numbers.
loop ends.

i incremented count 7 times.
my answer is `7`

let's try it out.

still TLE, passed more test cases, but still TLE.
it'd require another attempt.