# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/

i'm given a array of integers, called `nums`.

all the elements in `nums` are unique.

i can replace any integer within `nums`.

my job is to find out the least amount of replacements
i'd have to make, to make the array continuous.

***
what do you mean by make the array continuous?
when the array is continuous, every one step increment, starting from the smallest number?

***
what do you mean by make the array continuous?
a continuous array is this: if you incremented the smallest number by one

***
what's a continuous array, an array, when sorted, has it's element from smallest to largest differ by one digit.

***
what's a continuous array, is an array that you can iterate from the smallest element to the largest element?

***
a continous array is an array where every element has a left and right neighbor.

***
a continuous array is an array that can be arranged from smallest to largest, and every next element is +1 greater than the previous.

i.e. [3, 4, 2]

when you arrange, smallest to largest,
you'd have [2, 3, 4]
every next element from 2 till 4 is one greater than the previous.

***
where every number's next number is in the array.

***
a continuous array is an array where there's a sequence between the smallest number

***
a continuous array is an array where all the elements line up, and every next element is one integer bigger than the previous.

***
when we count integers, we go 1, 2, 3..
there's an order.

a continuous array is one where every element forms this order

***
all the elements are unique
all the elements follow each number when sorted
all the elements can follow each other

***
you don't know if it's continuous till you sort it.
or at least visually look for the smallest element, increment and check if the incremented number exists in the array.

the sort has to be in the definition.
a continuous array is one, when sorted in ascending order, has it's integers follow each other, as though one was counting the 1, 2, 3...

the following is a continuous array:
[4, 2, 5, 3]

because when you sort it, you have [2, 3, 4, 5]
and every element follows each other.
every element except the last of course.

okay, and what do i want to do?

the idea here is to sort first, the fill in the smallest gaps till we have `n` continuous numbers.

where `n` is the length of `nums`.

so i need to identify the gaps.
how do i do this?

if you sort the array, you can find the gaps
but what do you want to do with the gap?

you want to see if filling the smallest gap
gives you the number of continuous integers you want.

to be fair, the smallest gap is all you can pick.
any other gap you fill lengthens the number of replacements.

okay, and how do i know when i have continuous numbers
well, we can store number of continuous before each gap and number of continuous after each gap.

so with each gap we fill, we can tell, how much groud we've covered.
every gap we update should also update any gap neighbors it touches.

for instance if i have 2..4.5