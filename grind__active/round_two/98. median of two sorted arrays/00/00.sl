i'm given two arrays.

both arrays contain sorted integers.

i'm to return the median if both arrays were combined and sorted.

and, i'm to do this in O(log(m+n)) time.

this suggests binary search.

understandably so since the arrays are sorted.
**
what would the median look like?
well, the middle element.

if i line up all the elements of the array
counting them, i can figure out where the middle is.

the question is whether this middle element is in the 
first array or the second array.

if you have `7` elements, the middle element would be at `index 3`

but where would index 3 be?

for all i know the first index, index 0 could start the first array.

and the second array could start with index 5.
in that case, `index 3` would be in the first array.

but how would i know? i wouldn't.

i imagine most test cases would have the indices shuffled across both arrays.

what i do know is,

* both arrays are sorted.
* one of them has to be index 0
* one of them has to have the last index.

what do their midpoints say of each other.
if the mid point value of `firstArray` is less than the mid point value of the `secondArray`.

i'm not sure i can solve this on my own.

`https://www.youtube.com/watch?v=q6IEA26hvXc`
2:46

`the midpoint of the merged array has to exist in one of the arrays.

either exists in the longest one

or exists in two places.


if i have 13, elements, i know my mid point is 6
if i start off at that index 6 in the longest array

i ask does the start of the shorter array exceed the last value in the current array. if yes, we have our mid point.

if no, that midpoint should move to the left.

doing this, would shift some of those 6 elements into the other array.

now, i'd have a pivot in both arrays.

and the question to know if the pivot is valid.
if pivot in array1 less than the numbers after pivot2

and is value at pivot2 less than the numbers after pivot1

if both these things are true, we know where the median is relative to both arrays and can calculate from there.`
