what's the situation?

i want to write a class with two methods.

`addNum` and `findMedian`.

**
again..

i want to define an abstraction that is repeatedly given integers
and immediately knows the median of all the integers it's been given.

for this, i'm asked to implement two methods within a class.

`addNum` and `findMedian`

the functions do what they say.

how would implementation look like?

well, i'd need a way to store numbers in a way that allows me know the median.


TODO
there's a follow-up.

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution

If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

i'd address this once i have a working solution.

**
back to the question, i need a way to store numbers. a way that allows me retrieve the median instantly.

the median is the result of a the sorted numbers.

to keep the numbers sorted, i can use a heap. a min heap.
yes, this would sort the numbers, but it wouldn't tell me the median instantly.

the solution? two heaps.

how would this go?

a maxHeap and a minHeap, of roughly equal size.

imagine the numbers given are lined up in non-decreasing order.

the maxHeap would represent the first half.
the minHeap would represent the second half.

both heaps maintain individual sort orders, the upside of this is, i can immediately figure out the what numbers are the middle because they'd either be at the tip of both heaps or at the tip of one of them.

let's put this into perspective, if a number is added. how's it go?

by default place all numbers in the maxHeap.
say the first number is 6

maxHeap = [6]

say the next number is 4

maxHeap = [6, 4]

now, the rule is to maintain almost equal sizes between both heaps.
i'm jumping the gun regarding my explanation, i'm doing so because i know how the question goes.

i shouldn't.

let's restart.

**
i want to implement an abstraction that continuously stores integers and can immediately tell you the median of said integers.

to do this, i have to implement two methods, `addNum` and `findMedian`

to find the median, i need to sort the numbers.
however, the median retrieval wouldn't be immediate since i'd have to sort first.

so, the ideal way is to maintain a sorted order of the numbers.
a heap allows me store and sort numbers.

would this suffice? well, how would you find the median?
i'd need to know the numbers at the middle of sorting.

the heap doesn't give you this, it only sorts in ascending or descending order.

okay.. how about two min heaps? 

what's the idea here?

i'd maintain an equal split of the numbers i store.

this way the heaps could tell me what's at the middle immediately.
how would this go?

well, first, the numbers i've stored could be even or odd.
if even, two equal lengthed heaps would do.

if odd, one heap would have one more number than the other.

i get that but how would you know the middle? what kind of heaps?

min heaps or max heaps.

well, it depends on what you need, say you have two equal lengthed heaps.
what do you want to know?

from the first heap, i want to know the largest number
from the second heap, i want to know the smallest number

together these two will form the median.

following this, it makes sense for the first heap to be a maxHeap
and the second heap to be a min heap.

this also works for the case when the total numbers are odd in count.
i'd simply take the tip of the maxHeap, and that'd be my median.

okay, and how would adding the numbers go?

the first number can go in the max heap.
the next number can go where?
i'd still put it in the max heap.

the idea here is to always put the new number in the max heap.
then figure out if any overflow into the min heap.

an overflow would occur if the max heap had two items more than the min heap.
in which case, i'd pop the tip of the max heap into the min heap.

so at any point in time the max heap is at most one item ahead of the min heap.

i think this works, and what's finding the median like?

if even lengthed, take the tip of both heaps, sum up and divide by 2
if odd lengthed, take the tip of the max heap.

***
start here.

you want to implement an abstraction that continuously stores integers, and can retrieve the median of those integers in O(1) time.

for O(1) median retrieval, you'd need to have been storing these numbers in a sorted order.


you've deduced, you'd two heaps would help.
these heaps would each store half of the total numbers received.

if total numbers is odd.
one half would have one number more than the order.

you've also deduced you'd need a maxHeap for the left half.
and a minHeap for the right half.

when total numbers is even, the tip of the max heap and tip of the min heap
give you the middle two numbers, then you can average for median.

when total numbers is odd, the tip of the max heap is the median.

`the question now, is how do you maintain this split as you receive numbers?`