i'm given an array of integers.

the integers are sorted this way:

they start off in ascending order then descend.

if you could map the numbers on a number plane.
it would look like a mountain.

my job 

***

there's an array of integers, a sorted array of integers.

however, the sorting is done in a different way.

the integers start off ascending, then they descend.

for example:

[1, 2, 3, 2, 1]

the descent starts after `3`.

another thing is, this array cannot be accessed directly.
it's behind an abstraction called `MountainArray`.

this abstraction provides two methods.

`get(idx)` and `length()`

`get` returns the element at a specific index.
it doesn't say what happens if you pass a wrong index though.

and

`length` returns the number of elements in the array.

now, the task.
i'm given a number, `target`
and want to find out if this target exists within the array.

if it does, i'd return the target's index.
if it doesn't, i'd return `-1`

the abstraction only allows me make a `100` calls to `get` so i need to be efficient.

the sorted property of the array suggests binary search.
however, i'd need to tweak it.

for starters, i can get the middle element and compare with target.

on the lucky chance, middle element is target, i'd return the index.

if not, the big question:

`do i move left or move right?`

well, it depends on what part of the array we're in.
are we in the ascending part or the descending part.

how to find out?

if ascending:
    the number before would be less, or non-existent i.e. start of array.
    the number after would be greater, unless we're at the peak, at which point, it'd be lower.

if descending:
    the number after would be lesser, or non-existent i.e. end of array
    the number before would be higher, unless we're at the peak, at which point, it'd be lower

so i can figure out which part, ascent or descent.

***

if in ascent, what do i want to do?
    well, is the `target` greater than the current number.
    if it is move the left pointer to midPoint + 1

    and try again.

    if the `target` is less than current number.
    move the right pointer to midPoint - 1.

would any of this matter if we were at the peak or the start of the ascent.

if at the peak,
    moving left wouldn't matter.. it'd just be a regular binary search.

    moving right would take you into descent territory...`would it be easier to find the peak first then find target within ascent or descent?

or keep it as is.. where i'm trying the binary search on both parts at once?`


