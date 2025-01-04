# https://leetcode.com/problems/buy-two-chocolates/description/

# TODO https://neetcode.io/solutions/buy-two-chocolates
class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        pass
        prices.sort()
        two_cheap_chocs = prices[0] + prices[1]
        
        return money - two_cheap_chocs if money >= two_cheap_chocs else money
    
arr = [
    [[69,91,78,19,40,13], 94],
    [[98,54,6,34,66,63,52,39], 62],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.buyChoco(foo, bar)
print(res)