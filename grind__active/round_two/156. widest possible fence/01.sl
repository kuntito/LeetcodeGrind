i have a list of numbers.

i want to sum up distinct numbers and find the most occurring.

what makes this hard to write?
it's that the logic is dense.

you can combine any number with any number.

think about it like a pool of numbers.
a bag of numbers.

you can combine any number with any number.
but want to know what combination can occur the most.

assuming each number is used in a combination once.

i mean, the bag analogy holds this by default.

you pick a number, a number counts as a combination.
i can do that or combine the number with another.

the simplest case, is no combination.
i take every number as is.

then see what number appears the most.

but what if i combine.
it's really down to two options really.
take a number as it is, or combine it.

if i take it as it is, the question is
what's the most frequent combination in whatever's left.

it's recursive.
and if you'd combined it with another number.
it's what's the most frequent combination in whatever's left too.

so, how are you picking the first number,
well iterate left to right.

a pick is take out a number, explore the rest of the array.
it's simple to use a global set of omitted indices, or replace the value with None.

that's simpler.

so, you take planks with you.
iterate from left to right.

you have the bag.

pick a number.
i have, what can i do with rest.
    another recursive call.

what if i wanted to combine.
it's pick another number.
you'd basically sum.

so, iter left to right, default sum to 0.
on every increment, explore a new path.
the first instance is the picking a single number.

okay, so, at what point do you check the rest of the array.
i mean, you'd have to finish exploration to do this.

perhaps, keep track of every sum.