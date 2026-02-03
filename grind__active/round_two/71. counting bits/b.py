# https://leetcode.com/problems/counting-bits/

from typing import List

# i'm given an integer, `n` and want to return a list of integers

# but what happens in between..
# `n` helps me determine the size of the return array.

# the question says, the return array should be of size `n+1`
# okay..

# for each slot in the return array, let's call the array, `res`
# each slot in `res` has an index

# if `n = 2`
# you'd have an array with the indices.. 0, 1, 2

# for each slot, you want it's value to be the hamming weight of it's index.
# hamming weight is the total number of 1's in the binary representation of a number.

# `2` in binary is `10`
# so it's hamming weight is `1`

# how would this go..
# watched neetcode's video and the idea.. is there's repeated work

# 0 - 0000
# 1 - 0001
# 2 - 0010
# 3 - 0011
# 4 - 0100
# 5 - 0101
# 6 - 0110
# 7 - 0111
# 8 - 1000

# the conclusion with every new power of 2^?
# we'd have the answer by looking at previous bits and adding `1`

# the powers of 2 are 2^0, 2^1, 2^2
# which translates to 1, 2, 4..

# the idea is when we reach a new power of `2`
# the calculation for number of bits is `1` + the value `x` bits behind..

# if the current power of `2` is 2^0 = 1
# the number of bits at `1` is `1` + number of bits in the cell `1` bit behind..

# in essence arr[i] = 1 + arr[i - x]

# it seems confusing, because, i'm reusing `1` multiple times..
# but it's clearer with something like `4`

# at `4`, the current power of 2 is `4`
# rather, the current exponent of 2 `4`

# x = 4
# so arr[4] = 1 + arr[4-4]
# arr[4] = 1 + arr[0]
# which is still `1`

# when we get to the next number, `5`
# we do the same thing..

# arr[5] = 1 + arr[5 - 4]
# arr[5] = 1 + arr[1]
# in this case, it'd be `2`

# we keep doing this and would have populated the array

# error, updated current exponent to `n`
# instead of the current iterating index, `i`

class Solution:
    def countBits(self, n: int) -> List[int]:
        pass
        arr = [0]
        
        currentExp = 1
        for i in range(1, n + 1):
            # and how do we update `currentExp`
            # we update `currentExp` whenever `i` reaches a new exponent of `2`
            if (currentExp * 2) == i:
                currentExp = i
            
            arr.append(
                1 + arr[i - currentExp]
            )
            
        return arr
            
arr = [
    5,
]
foo = arr[-1]
sol = Solution()
res = sol.countBits(foo)
print(res)