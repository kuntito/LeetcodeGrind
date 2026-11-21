reet,

peeped neet's solution.

wanna understand it.

so, he's tracking, left to right,
the smallest number seen.

then in a stack, appends
the current number, and the the smallest number seen
as one array.

okay..
and at the start of each iteration.
...

you want to append (curNum, curSmallest)
however, you only want to this when
the stack is empty or when the last number in the stack
is bigger than current number.

okay..

the idea is to maintain a monotonically decreasing stack.
so you always want the items to go lower.

now each item in the stack,
also knows the smallest number before it.

each item, knows two things.
each item, tells you, at least two items are before where you're at.

and the solution is when the stack contains elements.
and the current number is what?

by the time we get here.
we know the current number is less than the last number
in the stack.

so, we only need to check that the current number
is greater and the smallest number before the last number in the stack.

but why does this work?

why store a decreasing amount of elements.
what does that do for you?