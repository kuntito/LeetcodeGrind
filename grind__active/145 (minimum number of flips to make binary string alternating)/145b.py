# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

# i want to implement `minFlips`, it takes one string argument, `s`
# and returns an integer.

# but what happens in between?
# `s` is a binary string, which means, it only contains zeros and ones
# i can only perform two types of operations on `s`

# operation type one and operation type two
# for type one, i can remove the character at the start of the string
# and append it to the end of the string

# for type two, i can pick any character in `s` and flip it's value.
# that is, flipping '0' turns it to '1'
# and flipping '1' turns it to '0'

# the question now becomes what's the minimum number of type-2 operations
# i need to perform such that `s` becomes alternating?

# alternating means no two adjacent characters are equal
# either a series of `01` or a series of `10`.

# how do i approach this situation?

# first of all, why don't i explore every character from a different starting point.
# what does that mean

# consider "abc"
# i can start at "a" then go to "b" then "c"
# i.e. a => b => c

# same vein, i can start at "b"
# and go "b" => "c" => "a"

# and finally,
# "c" => "a" => "b"

# well, yeah, but what's the point of this?
# aws gonna say it'd handle every possibly of type one operations
# so i could explore each permutation for the one closest to an alternating string
# but the counter argument is type one and type two opeartions can occur back to back
# it's not the case that i do all the type ones and then type two?

# consider, "111000"
# three ones and three zeros

# i see benefit of a type one first
# if i shift the first one to the end
# then i'm good innit

# it becomes "110001"
# now i have at least one "01"
# at the end, how can i make every thing else a "01" series

# first off, flip the first char
# now, we'd have
# "010001"

# and now we just have to flip the fourth char (index 3)
# "010101"

# and that's three operations in total.
# however the example shows it can be done in less, `2`.
# actually, i might still be right.

# we want the total number of type 2 operations
# in our case, we did do two type two operations
# i think my approach could still work

# exploring all the type ones for the best fit
# then applying type two to it.

# it would be remarkably inefficient
# but it should work.

# for each permutation, i want to check two things
# it's "01" count
# and it's "10" count

# whichever one is more is my guy...

class Solution:
    def minFlips(self, s: str) -> int:
        pass