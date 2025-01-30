# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

# TODO https://neetcode.io/solutions/count-odd-numbers-in-an-interval-range
class Solution:
    def countOdds(self, low: int, high: int) -> int:

        first_term = low if low % 2 else low + 1
        
        if first_term > high:
            return 0
        
        diff = 2
        
        # `n` is the number of odd numbers after the first one
        n = (high - first_term)//diff
        
        return n + 1
    
arr = [
    [3, 7],
    [798273637, 970699661],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.countOdds(foo, bar)
print(res)