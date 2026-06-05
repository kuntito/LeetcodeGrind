i have an object, it's called a mountain array.

it represents a sequence of numbers that increase then decrease.

a sample sequence is, 5 6 4

like a regular array, each number is indexed from 0 till 2.

i'm told to find the index of a number within the mountain array.
the smallest index of that number.

the reason, 'smallest' matters, is the numbers in the mountain array are not unique.

for example, 1 5 1, is a valid mountain array.

if i was told to find 1, my answer would be index 0.

consequently, if the number i seek does not exist in the mountain array.
i should return -1.

okay, how do i find this number?

since the numbers are sort of sorted, i can apply binary search.

problem is, i can't treat the entire array as a search space.

the increasing portion of the array can be addressed with binary search.

and i believe, the decreasing portion too..

but i'd need to find the point where this happens.