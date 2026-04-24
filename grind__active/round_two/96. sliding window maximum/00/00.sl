i have an array of integers, `nums`.

i have a window, the window is a smaller portion of the array.
a group of back to back elements within the array.

if nums = [1, 2, 3]

a window of size 2 could be [1, 2] or [2, 3].

now, the question.
given `nums` and a window of size `k`.

i want to move that window through the array, one step at a time.
and in each step, i want to note the largest number in the window
and store it.

when i'm done,
i want to return an array containing the largest numbers in each window.

for example:
nums = [1, 2, 3], k = 2

my windows are:
[1, 2] and [2, 3]

in [1, 2], my largest number is `2`
in [2, 3], the largest number is `3`

so i'd return [`2`, `3`]

and how would this go in code?

for the first window, check every element, note the highest one.

for subsequent windows, what are you doing? 
when you move the window, 

you essentially remove the earliest element from the window
then add a new element after the latest one.

so, if we know the largest element from a previous window.
we now need to know if it needs updating.

there's two scenarios:

* the earliest number we removed was the largest
* the earliest number we removed wasn't the largest

if we removed the the largest number,
    the question becomes, is the new number the largest or something else in between.

if the number we removed wasn't the largest, 
    the question becomes, is the new number larger than our established largest.
    
this second case is relatively simple to handle and it overlaps with the first case.

in both cases, we ask the question,
`is the new number larger than the established largest?`

if yes, update largest
if no, was the removed number the largest?
    if yes, what's the next largest number in the array?

    which is where the problem lies? do we iterate through the array again?

`    it might be simple to maintain a max heap for each window.
    and whenever we remove elements, we check if they're on top of the heap.

    if they are, remove them.
    if not, store them in a set.

    this way, when we need to find the next largest number within the window.
    we can simply take the top of the maxHeap provided the number on top isn't in the set.

    the set serves as an indicator that this number should have been removed.
    but we didn't have access to it at the time.`