# https://leetcode.com/problems/arranging-coins/

# TODO https://neetcode.io/solutions/arranging-coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # using a while loop with a condition that `n > 0`
        # decrement `n` by an `i`
        # `i` increases by one on each iteration
        # declare `res = 0`, increment it, everytime `(n-i) >= 0`

        res = 0
        i = 1
        while n > 0:
            n -= i 
            if n >= 0:
                res += 1
            i += 1

        return res