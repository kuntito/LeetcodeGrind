i'm given an array of integers, `nums`

i want to iterate through `nums`.
at each index,
i'd consider `k` consecutive numbers starting at that index.

for example, if nums is [10, 2, 18] and k is 2.

at index 0,
    the two consecutive numbers would be 10 and 2
at index 1,
    the two consecutive numbers would be 2 and 18
at index 2,
    i don't have two consecutive numbers, i have one.
    so, the iteration stops.

now, if k is 3, what happens?
at index 0,
    the three consecutive numbers would be 10, 2 and 18.
at index 1,
    i wouldn't have three consecutive numbers, i'd have two.
    and so the iteration stops.

the iteration only continues as long as i have `k` consecutive numbers from the current index.

this is called the sliding window.

now, for this question, i want to explore the sliding windows of size `k`
and in each window, i want to store the largest number.

when done with the iteration, i'd return the stored numbers in order.

***
so, how would this go?