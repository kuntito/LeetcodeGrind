step one is, create a grid.

a grid where each row represents each index within nums.

and each column represents what?

back up a bit.

***

step one, is to create a grid.

a grid where each row, represents each number in `nums`

and every column represents the total number of splits plus one.

why's there even a plus one.

it was added so.. column one meant split one.
and column two meant split two.

is that the fact? can't say for sure but it checks out.

what happens if you remove it?
at surface level, i'd have to deduct 1 from each split to get it's index.

to be frank, it's easier to reason about using the first column as a dummy.

column index 1, represents a split.
split 1?

well, not really, since the iteration is in reverse.
so, does it even help or am i capping.

if you're picking indices from behind and then you 

why's he even picking from behind?

perhaps, i need a high level overview of this joint.

'ccording to neet, he wrote this as a bottom up approach.

what does bottom up mean? it means you address the smallest case first then every bigger case.

and top down?
well, top down also addresses the smallest case first, then every bigger case.

the difference is in the approach. top down starts from the top element, and keeps digging till it finds the smallest case, then works it way back up.

while bottom up, starts from the smallest case, and then works it's way up.

in terms of work done, i'm not convinced they're doing anything much different.

and so, let's deep the algo in front of us.

you need to take a bottom up approach to solving this.

the first question is what's the smallest case.

last row, last column.

what's the question i'm asking there?

how many questions can i even ask there?