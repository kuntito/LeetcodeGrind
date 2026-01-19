# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# apparently, i'm playing a guessing game..
# LC guesses a number and i have to figure out what the number is..

# there's a function i didn't define called `guess`
# it takes one argument, an integer
# the point is, i'd use this function to find out, if my guess is correct

# the `guess` functions returns three situations, represented by a different integer
# my guess is correct, it returns `0`
# my guess is higher, it returns `-1`
# my guess is lower, it returns `1`

# so i'd keep guessing until i get the number..
# this joint is sounding like binary search...
# or sounding like it can be solved with binary search..
# where my guess is always the mid point..

# if i get it, i return the mid point..
# if my guess is lower, i move the right pointer to midPoint - 1


# what is this right pointer
# we're guaranteed number is not less than 1
# and not greater than 2^31 - 1

# so right pointer = 2^31 - 1
# left pointer = 1

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = 2**31 - 1
        
        while left <= right:
            myGuess = (right - left)//2 + left
            
            # i'd call the guess function
            guessResult = guess(myGuess)
            if guessResult == 0:
                return myGuess
            elif guessResult == -1:
                # my guess is higher..
                # move the right pointer to midPoint - 1
                right = myGuess - 1
            elif guessResult == 1:
                # my guess is too low..
                # it must on the right side of midPoint
                left = myGuess + 1