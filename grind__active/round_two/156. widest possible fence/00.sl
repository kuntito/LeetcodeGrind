i have planks. they all have a width of 1.
their heights vary, but i know their heights as well.

i want to build a fence which planks that all have the same height.

the question is in how many ways can you combine unique
numbers such that their height is the same?

there's probably some efficient way to do this.
but it seems like one would have to explore all combinations.

well for one, it's how many planks have the same height in the original array.

that's one answer.
can we find a better one.

well, pick one plank, compare it with every other plank.
see what it's new height gives as a result.

track that too.
then you can either combine the plank with another plank or pick a new plank.

it's feeling recursive.
you can pick a plank or combine it.
with every combination, you explore the rest of the array for what the combination holds.

so, how would 2, 3, 7 go?
you'd start with nothing,
so you either combine nothing with 2 or pick 3.

say we combine, we have 2, run the logic, our answer is 1.
say we pick 3, our answer is still 1.

then what?