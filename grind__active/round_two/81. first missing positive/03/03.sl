# https://leetcode.com/problems/first-missing-positive/description/

i have an array `nums`.

i want to find the smallest positive integer that's not in `nums`.

what does smallest positive integer mean?
well, of all the positive integers in `nums`, which is the smallest?

nah, that's not it.
what it is, is what's the smallest positive integer that's not in the array.

by default, the smallest positive integer is `1`.
if `1` is in the array.

the smallest positive integer would have to be `2`
if `2` is the array, then `3` and so on..

so i would always be moving forward until i hit the first number that's not in the array.

on one hand, i can run a loop from `1` onwards and keep checking for the first number that isn't in the array.

the challenge here is the O(1) space and the O(n) time. reason being, checking if a number is in the array requires me to either search through the array of use a set to store the available numbers.

if i search through the array, that's O(n) for every search.
that's potentially a O(n x n), if i have to search for every number.
clearly doesn't meet the constraints.

if i store the numbers in a set, i can search in O(1) time, iterate through all numbers in O(n) which would bring down O(n x n) to O(n x 1)

but even this violates the O(1) space.

one thing i do know is, i need to know the numbers that already exist in the array to determine the smallest positive integer.

and i think this is the hint to the question. the demand for O(1) space suggests i use the array as it's own storage.

but how?
how can i store numbers? rather? how can i check if a number exists in the array?

well, for one, i don't need to check all the numbers.
say i start at the first number, `1`

the question is, how can i check if `1` exists in the array without searching?

i'd say this is the core of the question.
i think the trick here is to sort the list.

but isn't sorting nlogn at best?
what do i really need?

i need to check if 1, 2, 3.. onwards exist in the array.
is there an upper limit for the numbers i'd need to check?

well, i'd say the largest integer.
but is that the case?

you're looking for the smallest positive integer not in the array.
what's the worst case scenario.

the worst case is all the numbers you check exist.
1, 2, 3, ...

but your limit would always be the size of the array.
if the array is of length `5`

your worst case becomes having to check
1, 2, 3, 4, 5

and then it ends, so you know `6` must be the answer.

so there's a limit to how many numbers i can check.
but this still doesn't answer the search?

well, it doesn't but it tells you, you only need to be concerned about numbers
1 through to array size.

but how does this tell me where the number is?
what if you move the numbers around?

what do you mean?
since i have a hard cap of array size as the highest number.
can i not map each small positive integer to it's index?

this way, the index serves as the storage.
if i'm looking for `1`, i know to check index `0`

if i'm looking for `2`, i know to check index `1`

if i'm looking for `5`, i know to check index `4`

this way, i've solved the searching problem.
but how do you get each number to it's index.

you can move them immediately.

since if you see a small positive integer
you immediately know where it should be.

that's an O(1) operation.
and what happens to the number at the index you're moving to.

well, you can move that too.

the thing is, if every small positive integer exists, 
they can be placed at the right index.

the only numbers that can't be placed are negative numbers, 0, or numbers greater than array size.

in which case, it wouldn't matter if you override them.
having moved numbers around, it now becomes a case of iterating through every number in `nums`

you expect to find `1` at index `0`
if you don't find `1`, it means `1` is missing from the array.

so the first index you get to where youb don't find the right number is your result.

the moving is also O(n) so
it answers the question's constraints of O(n) time and O(1) space.

so it's in two steps.

*   move existing small positive integers to right index.
*   iterate through `nums` to find the first number not at it's index.
    and if all numbers are at index, your result is `arraySize + 1`

PROBLEM 1:
i wrote this:
`
    def move(self, number, arr):
        # now, how do i move a number
        # well, where should the number go?
        # it should go to the index, `number - 1`
        
        # but first, we need to determine if the number should even move
        # keep in mind, we only want to move numbers between `1..arraySize`
        
        shouldMove = number in range(1, len(arr))
        if shouldMove:
            # then we move, but what if it's occupied
            # well, we should move the occupant to
            # so recursion.
            
            destinationIdx = number - 1
            occupant = arr[destinationIdx]
            
            self.move(occupant, arr)
            
            arr[destinationIdx] = number
`

but ran into an infinite recursion for a test case.
the problem here, is my `move` isn't exactly a move.

what i've done is duplicated the number at `destinationIdx`
a move is removing the number entirely from it's current index
then placing it at destination index.

PROBLEM 2:
to check whether to move a number, i wrote this:
`shouldMove = 1 <= number <= len(arr)`

the problem is, when `number` isn't always a number
and this isn't obvious to me, since `number` starts out as a number.

what happens is, i iterate through every number in `nums`
i iterate with index.

for each number, i verify if the number is at the right index.
if it isn't, i call `self.move`

the move operation dictates three things.
* make the current position vacant
* determine the new position and move any occupant.
* place the number at the new position.

the vacant step, i implemented by placing a `None`.
for the occupant, i simply call `self.move` on the occupant.

the problem is, it's possible, the occupant is `None`
and when i call `self.move`, it eventually runs this:
`shouldMove = 1 <= number <= len(arr)`

which breaks the code, since `number` is None
and you can't compare `None` with other numbers.

the function starts off requiring a number argument.
but because, i do a recursive move and use None to indicate vacancy,
i encounter this problem.

one solution is to check for `None`.
another is to use a number that wouldn't pass the `shouldMove` check.

the second solution is the simpler one.