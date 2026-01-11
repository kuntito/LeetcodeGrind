# https://leetcode.com/problems/stone-game/description/


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        pass
        # use a bottom-up dp approach
        li, ri, memo = 0, len(piles) - 1, {}
        return self.explore(li, ri, piles, memo) > 0

    def explore(self, li, ri, piles, memo):
        if li > ri:
            return 0
        
        mi = (li, ri)
        if mi in memo:
            return memo[mi]
        
        # since we only care about `aliceScore`, need to know when it's alice's turn
        isAliceTurn = True if self.is_range_even(li, ri) else 0
        
        
        # you can either pick from the left pile or the right pile
        # say we pick from the left pile, we determine `leftPick`
        
        # since we only track alice's score,
        # we only assign `leftPick` a value when it's alice's turn
        # when it's bob's turn the pick still happens, in the sense that 
        # `(li + 1, ri)` exclude it from the list
        
        # we just don't add it to our `cache`
        leftPick = piles[li] if isAliceTurn else 0
        
        # after picking the left, what happens if bob picks optimally 
        # from the rest of the range, `(li + 1, ri)`
        exploreLeftRes = leftPick + self.explore(li + 1, ri, piles, memo)
        
        # we do the same for our right picks
        # it only has a non-zero value when it's alice's turn
        rightPick = piles[ri] if isAliceTurn else 0
        
        # then we explore what happens when whoever has to pick from the rest of the pile
        # each recursive function simulates turn taking between alice and bob
        # since we know `piles` is even,
        # it's always alice's turn when the available range has an even count
        exploreRightRes = rightPick + self.explore(li, ri - 1, piles, memo)
        
        # and here we store, the best score for alice between left res and right res
        memo[mi] = max(
            exploreLeftRes,
            exploreRightRes
        )
        
        return memo[mi]
    
    def is_range_even(self, li, ri):
        dist = (ri - li) + 1
        return dist % 2 == 0
    
    
arr = [
    [3,2,10,4],
    [5,3,4,5],
    [3,7,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGame(foo)
print(res)