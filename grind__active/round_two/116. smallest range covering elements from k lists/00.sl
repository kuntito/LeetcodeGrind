# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

i'm given one item, a 2d array of integers.

it's an array where each element is an array.

i'm told each of the sub arrays is sorted in non-decreasing order.
what does non-decreasing order mean?

it means moving from the smallest to the largest number
you will never encounter a number that's smaller than the previous number.

only higher or the same.

now, my job is to find the smallest range that contains at least one number from each sub array.

***

i'm given an array.

an array of arrays.
it's called a 2d array.

it's an array where each element is an array.

for example,
[
    [1, 2],
    [3, 4]
]

now, i'm told, every sub-array is sorted in non-decreasing order.
what that means is, moving left to right, within the array,
the numbers either increase or remain the same index to index.

for example, both arrays qualify as non-decreasing:

[1, 2, 3] and [1, 1, 2]

there was never a better yesterday.

now, what i want is to find a range, that includes a number from each subarray.
what do you mean by range?

two numbers, say, `a` and `b`
a is smaller than or equal to b
and they indicate a group of increasing numbers from a to b

for instance, the range (2, 5)
contains the numbers `2, 3, 4, 5`

and this is equally a range, (2, 2)
it contains a single number, `2`.

and what determines the size of the range?
`b-a`

you subtract the smaller number from the maybe bigger number.

so i want to find the smallest range that contains a number from each list.

how would that go?

before i proceed, it's worth pointing out, if i ever find two ranges with the same size.

i.e. (2, 3) and (4, 5)
i should always pick the one with the smaller first number.

that said, backt to the question.
how do i find the range that contains a number from every sub-array.

for one, i can declare a big range.

then narrow it down.
is that what i want?

i'm not too sure.

what does a range that contains a number from every sub-array look like?
(smallestNumberInArray, largestNumberInSubArray)

i'd say this is the widest range.
now, how do i reduce this so i still have a number from each array represented.

if i wrote out all the numbers, does it solve the problem?
i think it does, it's get clearer where this range is.

what are you suggesting?
line up all the numbers, smallest to largest.

for each number, store it's row index.
now, we run a sliding window across the laid out numbers.

we're checking for the first window that contains all the indices.
once we have that, we have our answer.