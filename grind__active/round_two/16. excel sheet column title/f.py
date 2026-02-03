# https://leetcode.com/problems/excel-sheet-column-title/

# what's the situation?

# i'm given an integer and want to convert it to a string.

# how does the conversion go?

# the first 26 integers map to uppercase letters A..Z
# 1 => A
# 2 => B
# ...
# 26 => Z

# now after 26, you add a new letter to the left side..
# 27 => AZ

# to make clearer what's going on here..
# there's infinite slots to the left..

# each slot can take at most exponents of 26 numbers
# before moving it's maximum capacity to the next slot

# the first slot can take at most 26 numbers
# once, you hit 26 and add one more..

# you take the entire 26 to the next slot, the slot on the left
# inside the next slot, that 26 becomes `1`

# so it's effectively
# [1][1]
# this happens until the second slot hit's 26 too..

# [26][1]
# at this point, we add one more character.. to the second slot, and it takes it's
# entire 26 to a third slot

# to become
# [1][1][1]

# so, how would this work in code?
# recursion, since we're doing the same thing at each slot..

# okay.. and in each call, what are we doing..
# we always want to take two or multiples of 26 to the next slot..

# so what do we do.. we divmod by 26
# this way the quotient tells us how many multiples of 26 we have..
# the remainder tells us what should go in the current slot..

# it's worth pointing out, if we have no remainder..
# it means we take `quotient - 1` to the next slot..
# we're subtracting `1` because the current slot can take that..

# if we have a remainder, we can take the entire quotient to the next slot
# since the remainder is what should go into the slot..

# we keep doing this and creating more slots..
# we can use an array to store this..
# append each slot to the right..
# and reverse the entire array..

# if we want to be more explicit
# we could use a queue and actually add each slot from the left..
# an array would suffice..

# or do both to make sure you know what you talking about..
# let's do array first.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        self.num_to_alpha = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
        }
                
        arr = []
        
        self.explore(columnNumber, arr)
        
        return ''.join(arr[::-1])
    
    def explore(self, number, arr):
        # what's the base case, when `number` is `0`
        # take 26 divmod 26 = 1 rem 0
        # you put the entire 26 i.e. (1 multiple) into the current slot
        # you take 1 - 0 to the next slot..
        if number == 0:
            return
        
        multipes26, rem = divmod(number, 26)
        
        if rem == 0:
            arr.append('Z')
            multipes26 -= 1
        else:
            arr.append(
                self.num_to_alpha[rem]
            )
            
        self.explore(multipes26, arr)