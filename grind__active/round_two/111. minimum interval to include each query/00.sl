# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/

two inputs, one output.

i'm given two lists, 
    one is called `intervals`
    another is called `queries`

what do they mean?
well, `intervals` contains a list of intervals.
a start number and an end number. i.e. [1, 4]

while, `queries` simply contains numbers.
but what do these numbers mean?

each number is a query.
i'm asking a question of the `intervals` array.

and the question is, what's the smallest interval that meets this condition:

left <= queries[j] <= right

but what does this condition mean?
let's narrow it down.

`queries[j]` can mean any query, any number.
let's say `2`

so the equation becomes

left <= 2 <= right

what are left and right?
these are the start and end of an interval.

so i'm looking for an interval
i'm looking for the smallest interval 
whose start is less than or equal to the query number
and whose end is greater than or equal to the query number.

hence, 

`left <= queries[j] <= right`

and what determines the size of an interval?
this is how many numbers are within it.

the interval [1, 4]
is of size `4`, you have the number 1, 2, 3, 4 within it.
to calculate, you can do `right - left + 1`

one thought is to expand from the query.
what do you mean?

imagine the intervals were placed on a number line.
the start and end of each one.

the query would live in-between the smallest interval.
unless the smallest interval doesn't exist.

but if it does, it'd be the case that the smallest one.
would contain the query.

and so, if i check from the query leftwards
for the start of any interval, the first one i find, whose end is after the query must be the smallest interval.

is this always the case?

imagine your query was `2`
and the intervals you had were [0, 2] and [1, 16]

moving leftwards, you'd first encounter the start point `1`
it's size would be 16.

it's the first interval, whose end is after query but it's not the smallest size interval.
i'd have to explore further to find out.

so i'd hit `0` too, find it's size is `3`
and so i'd have found my answer, since there's no further starts leftwards.

so i can't simply pick the first start i see whose end is after the query.

***
another idea.

sort both lists.

`intervals` and `queries`

then address each query one after the other.
the idea here is..

for each query, you iterate through the intervals.
the iteration continues until you find an interval whose start is greater than query.

why am i doing this?
the point is, the answer must be one of the intervals i'd have iterated past.

to make my work simple, i can calculate the size of each interval
and store in a min heap.

what an i storing in a min heap.
the size and the end of the interval.

why these two?
the size ensures the tip of the min heap is always the smallest sized interval.

and what do you need the end for?
this tells you if said interval has an end that exceeds the query.

why not just store only sizes whose end exceed the query.
well, what if other queries need it?

how could they, you're running through the queries in order.
if the interval couldn't overlap the current query. it can't possibly overlap the next.

yes, but the idea here is the min heap serves as a cache.

it knows the size and end of preceeding intervals.
for the current query, i don't need to store the end of the interval

but for the next query, i do.
because, the iteration through a sort order only ensures the starts are the smallest.
i don't know if the end exceeds the next query.

and that's why i'd need it.

based of that, i can keep popping the heap till i find one that overlaps the query.
and if i don't, the question says the answer should be -1.

one more thing, i meant to return the result of the queries in order.
so i'd have to note the initial order before sorting.

i need to know the initial order.
for each query, i need to know it's index somewhere?

hashmap?

recreate queries such that each item is (query, idx)
then sort `queries`

when iterating?..
create the res array first of same size as queries
then use the index to place the result.
