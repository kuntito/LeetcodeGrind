i want to implement a class
that stores numbers.

and knows the median number in it's storage.

***

how would you implement this?

to know the median number, i need to know the order of numbers.

i can use a heap. this way, i know the order of all the numbers.
but that doesn't tell me the median.

how about two heaps.
one half of the numbers in one.
the other half in another.

and for the median, how does this help?
it'd be a max heap and a min heap.

the max heap, contains, the first half.
min, contains the second half.

this way, i can find the median.
since the tip of both heaps
tell me the center of distribution.

and how would storage go?

the first number goes in the max heap.
the second number goes where?

well, still max heap.
the new thing, is we'd observe the max heap has two elements
the min heap has none.

we want to maintain some sort of balance.
equal number or the max heap has one more number than the min heap.

why one more?
the numbers in storage can total even or odd.
if even, even split in both heaps.

if odd, put one more in the max heap.


so, back to where we were.
two numbers in the max heap.

we'd offload the tip into the min heap.
so, now they're equal.

the third number comes in.
it stays in the max heap.

it matches the constraint, since the max heap size
exceeds min heap by one.

however, there's more to the distribution
you want the max heap to contain the first half of the numbers.

and so..
if you have

[2,5] and [3]

you wouldn't be doing that.
well, how would i know if the distribution is valid.

whatever number you add to the max heap must be smaller than or equal to the tip of the min heap.

if that's the case, the number can stay there.
if not, remove the tip of the min heap.
add to the max heap.

then remove the tip of the max heap, add to the min heap.

so...
[2, 3, 5] and []

then..
[2, 3] and [5]

this way, the balance is always maintained.
and as such, i can find the median.