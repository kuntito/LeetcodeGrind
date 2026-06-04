i'm given two collections of numbers.

each collection is sorted.

i want to find the median number if both collections were combined.

and i want to do this in O(log(a + b)) time.

but what does this even mean?

it means O(log n), where n is `a + b`
the log n run time, means, every step, you reduce half the sample size.

this, essentially what binary search does.

and the reason the question says two variables in the log is cause,
i'm dealing with two collections.

it's telling me the algo would be log(n) and applied to both collections.

a single algorithm, that treats both collections as one.

i'd have to manage state.

what would it mean to treat both as one?

well, combine them without combining them.

if the numbers were combined, there'd be a start.
there'd be an end.

you can figure out which of the collections has the smaller start value.
and that's the start of the combined collection.


the collection with the bigger end value is the end of the combined collection.

so, i know the start, i know the end.

how do i find the middle?

the middle can still exist in either collection.

why even talk start and end? well, i felt it'd be easier to find the middle
once i know the start and i know the end.

but this info doesn't tell me where the middle is, does it?
how would i even know if i've reached the middle?

without the info in the other collection.

you need to know what's going on in both collections.

i know the shape of the answer.

but i can't derive it.

each collection has a index, 
who's value represents the median in the combined colelction.

is this true?
well, it's possible, the median exists in only one collection.

yeah, i've muddled my thinking.

i can't see the problem clearly.